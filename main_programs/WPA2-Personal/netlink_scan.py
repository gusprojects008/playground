import socket
import struct
import os

class nlmsg_types:
      # RTM Routing Table Management
      RTM_NEWLINK = 0x10 # DEC: 16
      RTM_DELLINK = 0x11 # DEC: 17
      RTM_GETLINK = 0x12 # DEC: 18
      RTM_SETLINK = 0x13 # DEC: 19
      RTM_NEWADDR = 0x14 # DEC: 20

      # NM Neighbour Management
      RTM_NEWNEIGH = 0x1E # DEC: 30
      RTM_DELNEIGH = 0x1F # DEC: 31
      RTM_GETNEIGH = 0x20 # DEC: 32

      # TC Traffic Control 
      TC_NEWQDISC = 0x24 # DEC: 36
      TC_DELQDISC = 0x25 # DEC: 37
      TC_NEWFILTER = 0x26 # DEC: 38
      TC_DELFILTER = 0x27 # DEC: 39
     	
      # GN Generic Netlink
      NLMSG_NOOP = 0x01 # DEC: 1
      NLMSG_ERROR = 0x02 # DEC: 2
      NLMSG_DONE = 0x03 # DEC: 3
      NLMSG_OVERRUN = 0x04 # DEC: 4

class nlmsg_flags:
      NLM_F_REQUEST = 0x01
      NLM_F_ACK = 0x04
      NLM_F_ROOT = 0x100
      NLM_F_MATCH = 0x200
      NLM_F_DUMP = NLM_F_ROOT | NLM_F_MATCH 
      
def unpack_kernel_response(nlmsg):
    kernel_response = f"\nKernel Response: {nlmsg.hex()}"
    return kernel_response

def scan_managed(interface):
    nlmsghdr = struct.pack("IHHII", struct.calcsize("IHHII")) # NETLINK HEADER MESSAGE nlmsghdr(len(32bits), type(16bits), flags(16bits), seq(32bits), pid(32bits))
    genlmsghdr = struct.pack() # GENERIC NETLINK HEADER genlmsghdr(cmd(8bits), version(8bits), reserved(16bits))
    genlattr = struct.pack() # ATRIBUTES NETLINK nlattr(len(16bits), type(16bits))
    try:
       with socket.socket(socket.AF_NETLINK, socket.SOCK_RAW, NETLINK_GENERIC) as sock:
            sock.bind((os.getpid(), 0))
            #sock.send()
            #sock.recv(65536)
    except Exception as error:
           print(f"Error {error}")	 	

