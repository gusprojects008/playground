import socket
import struct
import os

# THE NLMSG FOLLOW STANDARD FORMAT:(32b, 16b, 16b, 32b, 32b) BUT WITH VALUES COMPATIBLE WITH THE NETLINK PROTOCOL USED AT THE TIME!

def nlmsg_builder(genlmsg, nlattrs):
    try:
       nlmsg_len = struct.calcsize("IHHII") + len(genlmsg) + len(nlattrs)
       nlmsg = struct.pack("IHHII", nlmsg_len, 18,  
