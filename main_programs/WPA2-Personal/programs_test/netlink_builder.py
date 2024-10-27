import socket
import struct
import os

# The nlmsg follows the standard format: (32b, 16b, 16b, 32b, 32b) but values such as flags and types change according to the netlink socket type!

# nlmsg (32b, 16b, 16b, 32b, 32b)
# genlmsghdr (8b, 8b, 16b)
# nlattr (16b + payload, 16b) + payload

def nlmsg_builder(nlcmd, nlattr, type, flags, seq):
    try:
       nlmsg_len = struct.calcsize("IHHII") + len(nlcmd) + len(nlattr)
       nlmsg = struct.pack("IHHII", nlmsg_len, type, flags, seq, os.getpid()) + nlcmd + nlattr
       return nlmsg
    except Exception as error:
           print(f"Error {error}")
           return None

def parse_kernel_response(nlmsg_kernel):
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

          # Is need to cancel the first 2 bits, because: *multiples of 4 always have the first 2 bits nulled, that is: 00!
          # exemple: (0(00000000), 4(00000100), 8(00001000), 12(00001100), 16(00010000), etc...)  
          offset += (nla_len + 3) & (~ 3) # the "offset" receives the nla_len while is smaller that len(nlattrs_bytes) like this going to the next one nlattr and the "while" loop processing again nlattr!
                                          # why "(nla_len + 3) & (~ 3)"?  This is so that nla_len is rounded to a multiple of 4! just because the lengths of nlmsg and others byte packets in computer, are generally multiples of 4 for various reasons, so must be follow standard to interpret the messages!
                                          # first (nla_len + 3) This is used if nla_len is not a multiple of 4 or a odd number, and if nla_len is a multiple of 4 the value will not change, because:
                                          # rule 0: if a number odd is somed (+ 3) the result is a even number, and if even number is somed (+ 3) the result is a odd number! 
                                          # bitwise operations: "& AND" operation sets each bit to 1 if both bits are 1, "~ NOT" operation inverts all the bits!
                                          # so 3(00000011) when (~ 3) go (11111100) causing (cancel or reset) the first 2 bits (2, 1) thus returning only multiples of 4!
                                          # exemple: (nla_len(7) + 3) & (~ 3) # 10 is even number but is not a multiple of 4!
                                          # ((nla_len(10) + 3) == 10(00001010)) & ((~ 3) == - 4(11111100))
                                          # 00001010
                                          #    &
                                          # 11111100
                                          # 00001000(8)
                                          # so (00001010(10)) & 11111100(~3) only filters by multiples of 4, because all multiples of 4 have the first 2 bits as 0, because numbers that are not multiples of 4 or odd use the first 2 bits to form themselves, so when we reset them we only take the bits that are multiples of 4 from the original value that come after the first 2 bits, thus rounding to a multiple of 4 smaller than the original value, that is, the multiple of 4 before the current number, example: the current number 10 (00001010), the multiple of 4 before it: 8 (00001000)!
                                          # so the big secret is to do an "AND" operation between the current number (nla_len + 3 (so that the first 2 bits are added (and if the number is already a multiple of 4 the value 3 added will be canceled and will return the same number multiple of 4 at the beginning, and if it is not a multiple of 4 the value 3 will also be canceled and will then return only the bits multiple of 4 of the initial value)) and the "AND &" operation is done with the same number 00000011 (3) but the result of the "NOT" operation being: 11111100 (~ 3), (3 & ~ 3 = 0) meaning that if the first 2 bits are (0 and 1) they will return zero and will not be counted in the byte, thus always canceling the first 2 bits, thus always returning multiples of 4. 
                                          # the nla_len message must be a multiple of 4 to be correctly aligned in the memory addresses which are generally 32 bits or 64 depending on the processor architecture, using multiples of 4 to define the size of each message makes the processing of message information more standardized, efficient and easy to interpret and then move on to the next message, so the processor divides each message information according to the protocol and structure of the specific message.  
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
         family_id = parse_kernel_response(kernel_response)["nlattrs"]["CTRL_ATTR_FAMILY_ID"][2].strip(b"\x00").hex()
    return family_id 

#def nl80211_get_scan():
    
def nl80211_trigger_scan(iface):
    # get family nl80211
    nl80211_family = int(nl80211_get_family(), 16)

    #iface = struct.pack("H", iface)

    # genlmsg trigger scan, in a message of type nl80211 through of a netlink generic, the cmd and attr of message must of type nl80211
    genlmsghdr = struct.pack("BBH", 0x21, 0, 0)
    genlattrs_iface = struct.pack("HH", struct.calcsize("HH") + len(iface), 3) + iface
    genlattrs_
    nlmsg_scan = nlmsg_builder(genlmsghdr, genlattrs, nl80211_family, 1, 1)

    with socket.socket(socket.AF_NETLINK, socket.SOCK_RAW, 16) as sock:
         sock.bind((os.getpid(), 0))
         print(iface)
         sock.send(nlmsg_scan)
         print(sock.recv(65536))

interface_index = struct.pack("I", int(input("Type it interface index: ").strip()))

nl80211_trigger_scan(interface_index)
