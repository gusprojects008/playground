import struct
def mac_for_bytes(mac):
    return bytes(int(byte, 16) for byte in mac.split(':'))

mac_interface = 'a4:f9:33:ed:5b:75'
mac_byte = mac_for_bytes(mac_interface)
destiny_packet = b"\xff\xff\xff\xff\xff\xff"
bssid = b"\xff\xff\xff\xff\xff\xff"
header_radio = struct.pack('<H6s6s6s', 0x04, destiny_packet, mac_byte, bssid)

print(header_radio)
