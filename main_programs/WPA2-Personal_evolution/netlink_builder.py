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

    nlattrs_bytes = nlmsg_kernel[genlmsghdr_len:] # after the nlmsghdr and genlmsghdr, the nlattrs(netlink attributes) begin, which contain the informations
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
