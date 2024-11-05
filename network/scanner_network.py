from scapy.all import *
import psutil
import socket

# FUTURE FEATURES: TCP SCAN: SYN, SYN-ACK, ACK

# FEATURE: SCAN ARP PROBE NO INTERNET

class colors:
      red = "\033[31m"
      green = "\033[32m"
      blue = "\033[34m"
      cyan = "\033[36m"
      purple = "\033[35m"
      reset = "\033[0m"
      pink = "\033[95m"

      # FORMAT TEXT
      bright = '\033[1m'
      background_green = '\033[32m'
      background_red = '\033[41m'
      blink = '\033[5m'
      sublime = '\033[4m'

      # COLOR + BRIGHT
      sb = f'{bright}{sublime}'
      gb = f'{bright}{green}'
      bb = f'{bright}{blue}'

# LIST INTERFACES FROM DATA SET IN INTERFACES
def list_interfaces():
    interfaces = psutil.net_if_addrs()
    for interface in interfaces:	
        print(f"{colors.gb}{colors.sublime}{interface}{colors.reset} {interfaces[interface]}\n")

def get_address(interface):
    address_info = psutil.net_if_addrs()

    if interface in address_info:
       for info in address_info[interface]:
           if info.family == psutil.AF_LINK:
              return info.address
    else:
        return None

def scanner_arp():    
    interface = input("Type it interface for scan: ")
    mac_address = get_address(interface)

    if mac_address is not None:

       # PACKET ARP FOR SENT AND RECOGNITION OF LOCAL
       packet = Ether(dst="ff:ff:ff:ff:ff:ff", src=mac_address) / ARP(op=1, hwsrc=mac_address, pdst="192.168.0.0/24")

       # SENT PACKETS AND RECEIVED AT LAYER 2
       send_recv_packets, no_reply = srp(packet, iface=interface, timeout=5, verbose=True)

       for packets_send, packets_recv in send_recv_packets:
           if packets_recv:
              print(f"INFO PACKETS RECV: {packets_recv}\n")
              
              # GETTING INFO ABOUT ADDRESS OF HOST:
              try:
                 ip_host = packets_recv.src
                 info_host = socket.gethostbyaddr(ip_host)
                 print(info_host)
              except:
                    print(f"Dont not possible get info about host );")
           else:
               print(f"without packets response );")


list_interfaces()
scanner_arp()
