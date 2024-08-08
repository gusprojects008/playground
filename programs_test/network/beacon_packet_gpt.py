import socket
import struct
import psutil

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

radiotap_header_version = 0x00
radiotap_header_length = 0x0c
radiotap_flags = 0x000000
radiotap_dummy_field = 0x000000

frame_control = 0x4000  # TYPE BEACON PACKET
duration = 0x00
source_packet = b"\x00\x15\x12\x13\x14\x15"
destiny_packet = b"\xff\xff\xff\xff\xff\xff"
bssid = b"\xff\xff\xff\xff\xff\xff"
sequence_packet = 0x00

ssid_element_id = 0x00
ssid_element_length = 0x00

supported_rates_element_id = 0x01
supported_rates_length = 0x08
supported_rates = b''.join(bytes([rate]) for rate in [0x82, 0x84, 0x8b, 0x96, 0x24, 0x30, 0x48, 0x6c])  # Taxas (1, 2, 5.5, 11, 18, 24, 36, 54 Mbps)

def show_interfaces_addrs():
    try:
       address_interfaces = psutil.net_if_addrs()
       for interfaces in address_interfaces:
           for info in address_interfaces.get(interfaces):
               if psutil.AF_LINK in info:
                  print(f"{colors.green}{info.address} => {colors.gb}{interfaces}{colors.reset}")
    except Exception as error:
           print(f"Error to get interfaces and address );\n{colors.red}{str(error)}{colors.reset}")

def send_packets_beacon():
    header_radiotap = struct.pack('<BBHI', radiotap_header_version, radiotap_header_length, radiotap_flags, radiotap_dummy_field)
    header_mac = struct.pack('<HH6s6s6sH', frame_control, duration, source_packet, destiny_packet, bssid, sequence_packet)
    ssid_info = struct.pack('<BB', ssid_element_id, ssid_element_length)
    rates_velocity = struct.pack('<BB', supported_rates_element_id, supported_rates_length) + supported_rates

    packet_beacon = header_radiotap + header_mac + ssid_info + rates_velocity

    print(f"{colors.cyan}Beacon Packet: {colors.reset}{packet_beacon}\n")

    try:
        sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
        sock.bind(('wlan0', 0))  # Use a interface no modo monitor
        sock.send(packet_beacon)
        print(f"{colors.green}Beacon packet sent successfully!{colors.reset}")
    except Exception as error:
        print(f"{colors.red}Failed to send beacon packet: {str(error)}{colors.reset}")

show_interfaces_addrs()
send_packets_beacon()
