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
    bright = '\033[1m'
    background_green = '\033[32m'
    background_red = '\033[41m'
    blink = '\033[5m'
    sublime = '\033[4m'
    sb = f'{bright}{sublime}'
    gb = f'{bright}{green}'
    bb = f'{bright}{blue}'

radiotap_header = b'\x00\x00\x12\x00\x2e\x48\x00\x00\x00\x02\xa0\x20'
frame_control = struct.pack('<H', 0x8000)
duration = struct.pack('<H', 0xFFFF)
destiny_packet = b"\xff\xff\xff\xff\xff\xff"
source_packet = b"\xaa\xbb\xcc\xdd\xee\xff"  # Substitua pelo MAC da sua interface em modo monitor
bssid = b"\xaa\xbb\xcc\xdd\xee\xff"  # Substitua pelo MAC do seu AP
seq = struct.pack('<H', 0)

# Elementos de beacon
timestamp = struct.pack('<Q', 0)
beacon_interval = struct.pack('<H', 0x0064)
capability_info = struct.pack('<H', 0x0431)

# SSID
ssid_element_id = struct.pack('<B', 0)
ssid_length = struct.pack('<B', len("TestSSID"))
ssid = b"TestSSID"

# Supported Rates
supported_rates_element_id = struct.pack('<B', 1)
supported_rates_length = struct.pack('<B', 8)
supported_rates = struct.pack('<BBBBBBBB', 0x82, 0x84, 0x8b, 0x96, 0x24, 0x30, 0x48, 0x6c)

# Construção do pacote beacon
beacon_frame = (
    frame_control +
    duration +
    destiny_packet +
    source_packet +
    bssid +
    seq +
    timestamp +
    beacon_interval +
    capability_info +
    ssid_element_id +
    ssid_length +
    ssid +
    supported_rates_element_id +
    supported_rates_length +
    supported_rates
)

# Cabeçalho radiotap + frame beacon
packet = radiotap_header + beacon_frame

def show_interfaces_addrs():
    try:
        print()
        address_interfaces = psutil.net_if_addrs()
        for interfaces in address_interfaces:
            for info in address_interfaces.get(interfaces):
                if psutil.AF_LINK in info:
                    print(f"{colors.green}{info.address} => {colors.gb}{interfaces}{colors.reset}")
    except Exception as error:
        print(f"Error to get interfaces and address );\n{colors.red}{str(error)}{colors.reset}")

def return_addresses(interface_network):
    addresses_interface = psutil.net_if_addrs()
    if interface_network in addresses_interface:
        for info in addresses_interface.get(interface_network):
            if psutil.AF_LINK in info:
                return info.address
    return None

def mac_for_bytes(mac):
    return bytes(int(byte, 16) for byte in mac.split(':'))

def send_packets_beacon(interface_network):
    try:
        print(f"\n{colors.bright}INTERFACE IN OPERATION:{colors.reset} {colors.gb}{interface_network}{colors.reset}")
        print(f"\n{colors.gb}PACKAGE SENT =>{colors.reset} {colors.red}{packet}{colors.reset}")
        
        sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
        sock.bind((interface_network, 0))
        sock.send(packet)
    except Exception as error:
        print(f"An error occurred: {colors.red}{str(error)}{colors.reset}")

show_interfaces_addrs()

interface_net = input("Type the network interface (e.g., wlan0): ")

if interface_net:
    send_packets_beacon(interface_net)
