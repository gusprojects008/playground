import socket
import struct
import os
import random
import time

# The nlmsg follows the standard format: (32b, 16b, 16b, 32b, 32b) but values such as flags and types change according to the netlink socket type!

# nlmsg (32b, 16b, 16b, 32b, 32b)
# genlmsghdr (8b, 8b, 16b)
# nlattr (16b + payload, 16b) + payload

def nlmsg_builder(nlcmd, nlattr, type, flags, seq):
    try:
       if isinstance(nlattr, list):
          nlattr_bytes = b''.join(nlattr)
       else:
           nlattr_bytes = nlattr
 
       nlmsg_len = struct.calcsize("IHHII") + len(nlcmd) + len(nlattr_bytes)
       nlmsg = struct.pack("IHHII", nlmsg_len, type, flags, seq, os.getpid()) + nlcmd + nlattr_bytes
       return nlmsg
    except Exception as error:
           print(f"Error {error}")
           return None

def parser_kernel_response(nlmsg_kernel):
    nlmsghdr = struct.unpack("IHHII", nlmsg_kernel[:struct.calcsize("IHHII")])
    nlmsghdr_len = struct.calcsize("IHHII")

    genlmsghdr = struct.unpack("BBH", nlmsg_kernel[nlmsghdr_len:nlmsghdr_len + struct.calcsize("BBH")])
    genlmsghdr_len = nlmsghdr_len + struct.calcsize("BBH")

    nlmsg_response = {}
    nlmsg_response["nlmsghdr"] = nlmsghdr
    nlmsg_response["genlmsghdr"] = genlmsghdr
    nlmsg_response["nlattrs"] = {}

    nlattrs_bytes = nlmsg_kernel[genlmsghdr_len:]
    offset = 0 # the offset is the starting point for data parse!

    while offset < len(nlattrs_bytes): #len(nlattrs_bytes): "while" Loop for the "offset", so we can increment the "offset" with the size of each nlattr message and thus iterate through the data!
          #nla_len, nla_type = struct.unpack("HH", nlattrs_bytes[offset:offset + struct.calcsize("HH")]) 
          nla_len, nla_type = struct.unpack_from("HH", nlattrs_bytes, offset)

          nlattr = nlattrs_bytes[offset:offset + nla_len] # Extract the nlattrs based on nla_len size! it is necessary for offset to receive the first nla_len to process the first nlaattr message, and then the loop for "offset" occurs again receiving "nla_len" thus going to the next message!
          nla_fmt = f"HH{nla_len - struct.calcsize('HH')}s" # Format used for struct.unpack() unpack bytes based in nla_len

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

          # offset receives just nla_len mutiple of 4
          offset += (nla_len + 3) & (~ 3)  

    return nlmsg_response
    
def nl80211_get_family():
    # NETLINK GENERIC = 16, GENL_ID_CTRL(min type for genlmsg) = 0x10(16)
    with socket.socket(socket.AF_NETLINK, socket.SOCK_RAW, 16) as sock: # generic netlink socket
         genlmsghdr = struct.pack("BBH", 3, 1, 0) # genlmsghdr cmd
         genlattr = struct.pack("HH", struct.calcsize("HH") + len(b"nl80211\x00"), 2) + b"nl80211\x00" # "\x00" means the end of a string, it is very important to use "\x00" for the netlink protocol to understand that it is a string, per because C language.
         nlmsg_generic = nlmsg_builder(genlmsghdr, genlattr, 0x10, 1, 1) #, pid) # genlmsg netlink

         sock.bind((os.getpid(), 0))
         sock.send(nlmsg_generic)

         kernel_response = sock.recv(65536)
         family_id = parser_kernel_response(kernel_response)["nlattrs"]["CTRL_ATTR_FAMILY_ID"][2].strip(b"\x00").hex()
    return family_id

def nl80211_get_scan(nl80211_familyID, iface):
    genlmsghdr = struct.pack("BBH", 0x20, 0, 0)
    nlattr = struct.pack("HH", struct.calcsize("HH") + len(iface), 0x03) + iface
    nlmsg = nlmsg_builder(genlmsghdr, nlattr, nl80211_familyID, 1 | 4 | (0x100 | 0x200), 1)

    return nlmsg

def random_mac():
    mac = [random.randint(0x00, 0xFF) for _ in range(6)]
    return ':'.join(f"{hex_byte:02x}" for hex_byte in mac)

def nl80211_trigger_scan(iface):
    # get family nl80211
    nl80211_family = int(nl80211_get_family(), 16)

    # genlmsg trigger scan, in a message of type nl80211 through of a netlink generic, the cmd and attr of message must of type nl80211
    genlmsghdr = struct.pack("BBH", 0x21, 0, 0)
    nl80211_nlattr_iface = struct.pack("HH", struct.calcsize("HH") + len(iface), 3) + iface

    # if want "probe response", put value 4 for ssid scan
    nl80211_nlattr_max_ssids = struct.pack("HHI", struct.calcsize("HHI"), 0x2d, 0)

    # ALSO IS POSSIBLE USE THE "OR" OPERATOR FOR EACH FLAG, EX: (1 << 1) | (1 << 2). FOR SO SEND THE TOTAL VALUE OF ALL FLAGS!
    nl80211_nlattr_flags = struct.pack("HHI", struct.calcsize("HHI"), 0x9e, 1 << 1)

    nl80211_nlattrs = [nl80211_nlattr_iface, nl80211_nlattr_max_ssids, nl80211_nlattr_flags]

    nlmsg_scan = nlmsg_builder(genlmsghdr, nl80211_nlattrs, nl80211_family, 1, 1)
    nlmsg_get_scan = nl80211_get_scan(nl80211_family, iface)

    with socket.socket(socket.AF_NETLINK, socket.SOCK_RAW, 16) as sock:
#         sock.setsockopt(270, 1, 1)
         sock.bind((os.getpid(), 0))
         sock.send(nlmsg_scan)
         time.sleep(10)
         sock.send(nlmsg_get_scan)
         kernel_response = parser_kernel_response(sock.recv(65536))
         print(sock.recv(65536)) #, kernel_response)
         
interface_index = struct.pack("I", int(input("Type it interface index: ").strip()))

nl80211_trigger_scan(interface_index)
#print(nl80211_get_family())
