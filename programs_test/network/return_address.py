import struct
import psutil

interface = input("Type it Interface: ")

def return_addresses(interface_network):
    addresses_interface = psutil.net_if_addrs()
    if interface_network in addresses_interface:
       for info in addresses_interface.get(interface_network):
           for address in info:
               if psutil.AF_LINK in info:
                  return info.address

def transform_mac_hex(mac):
    return bytes(int(byte, 16) for byte in mac.split(':'))
    

mac_interface = return_addresses(interface)

mac_hexdecimal = transform_mac_hex(mac_interface)

print(mac_interface, mac_hexdecimal)

hex_value = '0xff'

print(int(hex_value, 16))
