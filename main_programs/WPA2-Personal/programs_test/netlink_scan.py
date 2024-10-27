import socket
import struct
import os 

def unpack_kernel_response(nlmsg):
    kernel_response = f"Kernel Response: {nlmsg.hex()}"
    return kernel_response

def nlmsg_():
    nlmsg = struct.pack("IHHII", )
    genlhdr = struct.pack("")
def build_nlmsg_scan(iface_index):
    nlattr_family = b"nl80211".ljust(8, b"\x00")
    nlattr = struct.pack("I", iface_index)
    # 0x2d ATTR_SCAN_SSIDS, 0x45 NL80211_ATTR_TESTDATA, 0x9e NL80211_ATTR_SCAN_FLAGS
    nl80211_attrs = struct.pack("HHI", struct.calcsize("HHI"), 0x2d, 0x04) + struct.pack("HHI", struct.calcsize("HHI"), 0x9e, 16384)

    nlmsg_len = struct.calcsize("IHHII") + struct.calcsize("BBH") + struct.calcsize("HH") + len(nlattr) + len(nl80211_attrs)
    
    # nlmsg_type is NL80211 FAMILY ID 0X26
    nlmsghdr = struct.pack("IHHII", nlmsg_len, 0x26, 0x01 | 0x04, 1, os.getpid()) # NETLINK DEFAULT HEADER MESSAGE nlmsghdr(len(32bits), type(16bits), flags(16bits), seq(32bits), pid(32bits))
    genlmsghdr = struct.pack("BBH", 0x21, 0, 0) # OPERATION NETLINK, GENERIC NETLINK HEADER genlmsghdr(cmd(8bits), version(8bits), reserved(16bits))
    genlattr = struct.pack("HH", struct.calcsize("HH") + len(nlattr), 0x3) + nlattr

    nlmsg = nlmsghdr + genlmsghdr + genlattr + nl80211_attrs
    return nlmsg

def scan_managed():
    try:
       with socket.socket(socket.AF_NETLINK, socket.SOCK_RAW, 16) as sock:

            attr_family = b"nl80211".ljust(8, b"\x00")
            nlmsg_len = struct.calcsize("IHHII") + struct.calcsize("BBH") + struct.calcsize("HH") + len(attr_family)
            nlmsghdr = struct.pack("IHHII", nlmsg_len, 0x10, 0x01 | 0x04, 1, os.getpid()) # NETLINK DEFAULT HEADER MESSAGE nlmsghdr(len(32bits), type(16bits), flags(16bits), seq(32bits), pid(32bits))
            genlmsghdr = struct.pack("BBH", 3, 1, 0) # OPERATION NETLINK, GENERIC NETLINK HEADER genlmsghdr(cmd(8bits), version(8bits), reserved(16bits))
            genlattr = struct.pack("HH", struct.calcsize("HH") + len(attr_family), 2) + attr_family # ATRIBUTES NETLINK nlattr(len(16bits), type(16bits))
            nlmsg = nlmsghdr + genlmsghdr + genlattr # NETLINK ROUTE SOCKET TO GET LINK INFORMATIOS INTERFACES HARDWARE

            sock.bind((os.getpid(), 0))

            nlmsg_trigger_scan = build_nlmsg_scan(4)
            sock.send(nlmsg_trigger_scan)
            print()

            kernel_response = sock.recv(65536)
            print(kernel_response)

    except Exception as error:
           print(f"Error {error}")
           sock.close()

scan_managed()
