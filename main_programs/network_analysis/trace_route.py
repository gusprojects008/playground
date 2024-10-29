# THIS PROGRAMS CAPTURE ALL ROTATINS OF A PACKET SEND, AND SHOW INFORMATIONS ABOUT IT!
# TRACEROUTE SEND PACKETS ICMP AND UDP JUST

from scapy.all import *
import socket
import requests
import json

# CODES ANSI FOR COLERED THE TERMINAL AND TEXT APRESENTED FOR USER
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

# FLAGS FOR ALERT THE USER
class flags:
      ok = f'{colors.bright}{colors.green}[ * ]{colors.reset}'
      error = f'{colors.bright}{colors.red}[ * ]{colors.reset}'
      finalization = f'{colors.purple}{colors.bright}[ * ]{colors.reset}'

# TRY GET HOSTNAME OF MACHINE FROM IP
def hostname_ip(ip):
    try:
       host = socket.gethostbyaddr(ip)
       print(host)
    except socket.herror as error:
           print(f"{flags.error} ERROR: {str(error)}")

def location_ip(ip):
    get_info = requests.get(f"https://ipinfo.io/{ip}/json")
    json_format = json.loads(get_info.text)
    info_full = f"{json_format['city']}\n{json_format['region']}\n{json_format['country']}\n{json_format['loc']}\n{json_format['org']}\n{json_format['postal']}\n{json_format['timezone']}"
    print(info_full)

def traceroute_func():
    # TCP SYN
    target_ip = input("Type it your target IP: ")
    des_port = int(input("Type it your destiny port of target: "))
    interface = input("Type it your interface adapter Network: ")
    ttl_user = int(input("Type the Time To Live(ttl) of the packet, max*64: "))
    
    packet = [IP(dst=target_ip, ttl=ttl_user) / TCP(dport=des_port)]
    print(f"\n{flags.ok}{colors.red} packets sent:{colors.gb} {packet} {colors.reset}\n")
    packet_recv_send = sr1(packet, iface=interface, timeout=5)
    print(f"\n{colors.gb}RESPONSE:{colors.reset}\n")

    if packet_recv_send:
       print(packet_recv_send.show())
       hostname_ip(packet_recv_send.src)

       print(f"{flags.ok}{colors.bb} INFORMATIONS IP {packet_recv_send.src}:{colors.reset}")
       try:
          location_ip(packet_recv_send.src)
       except Exception as error:
              print(f"{flags.error}{colors.red} Error: Dont possible get informations of the ip address {str(error)}{colors.reset}")
    else:
        print(f"{flags.error}{colors.bb} NOT RESPONSE );{colors.reset}")

    # INIT TRACEROUTE
    # SENDING PACKETS UDP AND ICMP JUST
    print()
    location_ip(target_ip)
    print(f"\n{flags.ok}{colors.blue} sending packets ICMP and UDP... trace route:{colors.reset}\n")
    print(f"{colors.gb}RESPONSE:{colors.reset}\n")
    packets_sent_recv, ananswered = traceroute(target=target_ip, dport=des_port, maxttl=ttl_user)

    for packet_sent, packet_recv in packets_sent_recv:
        if packet_recv:
           print(f"\n{colors.gb}{packet_recv.summary()}{colors.reset}")
           hostname_ip(packet_recv.src)

           print(f"{flags.ok}{colors.bb} INFORMATIONS IP {packet_recv.src}:{colors.reset}")
           try:
              location_ip(packet_recv.src)
           except Exception as error:
                  print(f"{flags.error}{colors.red} Error: Dont possible get informations of the ip address {str(error)}{colors.reset}")
        else:
            print(f"{flags.error}{colors.bb} NOT RESPONSE );{colors.reset}")

traceroute_func()
