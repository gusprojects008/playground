from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, UDP
from scapy.layers.dhcp import DHCP, BOOTP, RandInt
from scapy.sendrecv import srp, sendp, srp1, sniff
from io import StringIO
import sys

def handle_packets(packet):
    if packet.haslayer(DHCP) or packet.haslayer(BOOTP):
       dhcp_info_options = packet[DHCP].options
       dhcp_yiaddr = packet[BOOTP].yiaddr
       print(dhcp_info_options)
       print(f"\nAddress offered: {dhcp_yiaddr}\nsubmask_net: {packet[DHCP].options[3][1]}")
    else:
        print("DHCP OR GATEWAY SERVER NO RESPONSE ):")
       
def dhcp_discover():
    mac_address = 'a4:f9:33:ed:5b:75'
    mac_broadcast = 'ff:ff:ff:ff:ff:ff'

    dhcp_options = [('message-type', 'discover'), ('requested_addr', '192.168.0.100'), 'end']

    dhcp_packet = Ether(dst=mac_broadcast, src=mac_address) / IP(src='0.0.0.0', dst='255.255.255.255') / \
                  UDP(sport=68, dport=67) / BOOTP(op=1, chaddr=mac_address, xid=RandInt(), flags=0x8000) / \
                  DHCP(options=dhcp_options)

    # YOU NOT RECEIVED A RESPONSE DIRECTLY OF THE SERVE DHCP, THE SRP1 NOT WORKING FOR THIS CASE!
    send_recv_packets = sendp(dhcp_packet, iface='wlan0')

    sniff(filter="udp and (port 67 or port 68)", iface="wlan0", timeout=10, store=True, prn=handle_packets)
    
dhcp_discover()
