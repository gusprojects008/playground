import socket
import struct
import os

# THE NLMSG FOLLOW STANDARD FORMAT:(32b, 16b, 16b, 32b, 32b) BUT WITH VALUES COMPATIBLE WITH THE NETLINK PROTOCOL USED AT THE TIME!

def nlmsg_builder(nlcmd, nlattr, type, flags, seq):
    try:
       nlmsg_len = struct.calcsize("IHHII") + len(nlcmd) + len(nlattr)
       nlmsg = struct.pack("IHHII", nlmsg_len, type, flags, seq, os.getpid()) + nlcmd + nlattr
       return nlmsg
    except Exception as error:
           print(f"Error {error}")

def parse_kernel_response(nlmsg_kernel):
    nlmsghdr = struct.unpack("IHHII", nlmsg_kernel[:struct.calcsize("IHHII")])
    nlmsghdr_len = struct.calcsize("IHHII")

    genlmsghdr = struct.unpack("BBH", nlmsg_kernel[nlmsghdr_len:nlmsghdr_len + struct.calcsize("BBH")])
    genlmsghdr_len = nlmsghdr_len + struct.calcsize("BBH")

    nlmsg_response = {}
    nlmsg_response["nlmsghdr"] = nlmsghdr
    nlmsg_response["genlmsghdr"] = genlmsghdr
    nlmsg_response["nlattrs"] = {}

    # after the nlmsghdr and genlmsghdr, the nlattrs(netlink attributes) begin, which contain the informations

    nlattrs_bytes = nlmsg_kernel[genlmsghdr_len:]
    offset = 0

    while offset < len(nlattrs_bytes): #len(nlattrs_bytes):  # the offset is the starting point for data parse!
          #nla_len, nla_type = struct.unpack("HH", nlattrs_bytes[offset:offset + struct.calcsize("HH")]) 
          nla_len, nla_type = struct.unpack_from("HH", nlattrs_bytes, offset)

          nlattr = nlattrs_bytes[offset:offset + nla_len] 
          nla_fmt = f"HH{nla_len - struct.calcsize('HH')}s"

          if nla_type == 1:
             nlmsg_response["nlattrs"]["CTRL_ATTR_FAMILY_ID"] = struct.unpack(nla_fmt, nlattr)
          elif nla_type == 2:
               nlmsg_response["nlattrs"]["CTRL_ATTR_FAMILY_NAME"] = struct.unpack(nla_fmt, nlattr)
          elif nla_type == 3:
               nlmsg_response["nlattrs"]["CTRL_ATTR_VERSION"] = struct.unpack(nla_fmt, nlattr)
          elif nla_type == 4:
               nlmsg_response["nlattrs"]["CTRL_ATTR_HDRSIZE"] = struct.unpack(nla_fmt, nlattr)               
          elif nla_type == 5:             
               nlmsg_response["nlattrs"]["CTRL_ATTR_MAXATTR"] = struct.unpack(nla_fmt, nlattr)
          elif nla_type == 6:             
               nlmsg_response["nlattrs"]["CTRL_ATTR_OPS"] = struct.unpack(nla_fmt, nlattr)           
          else:
              pass 

          offset += (nla_len + 3) & ~3
          
    # "while" Loop for the "offset", so we can increment the "offset" with the size of each nlattr message and thus iterate through the data!
    # Extract the nlattrs based on nla_len size!
    # the "offset" receives the nla_len while is smaller that len(nlmsg_kernel) like this going to the next one nlattr and the "while" loop processing again nlattr!

    return nlmsg_response
    
def get_familyID_nl80211():
    # NETLINK GENERIC = 16, GENL_ID_CTRL(min type for genlmsg) = 0x10(16)
    with socket.socket(socket.AF_NETLINK, socket.SOCK_RAW, 16) as sock:         
         genlmsghdr = struct.pack("BBH", 3, 1, 0)
         genlattr = struct.pack("HH", struct.calcsize("HH") + len(b"nl80211\x00"), 2) + b"nl80211\x00" # "\x00" means the end from a string, is very important use "\x00" for protocol netlink understand that is a string.
         nlmsg_generic = nlmsg_builder(genlmsghdr, genlattr, 0x10, 1, 1)

         sock.bind((os.getpid(), 0))
         sock.send(nlmsg_generic)

         kernel_response = sock.recv(65536)
         print(parse_kernel_response(kernel_response))

         #print(struct.unpack("I", parse_kernel_response(kernel_response)["nlattrs"]["CTRL_ATTR_HDRSIZE"][2]))

def nl80211_scan(iface):
    genlmsghdr = struct.pack("BBH", 3, 1, 0)
    genlattr = struct.pack("HH", struct.calcsize("HH") + len(b"nl80211\x00"), 2) + b"nl80211\x00"

    nlmsg_type = get_familyID_nl80211()
    print(nlmsg_builder(genlmsghdr, genlattr, 0x10, 0x01, 1, 1))
    print('\n', nlmsg_type)
#nl80211_scan(1)

get_familyID_nl80211()
