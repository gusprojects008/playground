import socket
import psutil
import struct

radiotap_header_version = 0x00
radiotap_header_length = 0x00
radiotap_flags = 0x00
radiotap_dummy_field = 0x00

frame_control = 0x4000  # TYPE BEACON PACKET
duration = 0x00
#source_packet = b"\x00\x15\x12\x13\x14\x15" # \x IS USED FOR REPRESENT A VALUE HEXDECIMAL IN A STRING AND 0x IS USED FOR REPRESENT A VALUE HEXDECIMAL PURE 
destiny_packet = b"\xff\xff\xff\xff\xff\xff"
bssid = b"\xff\xff\xff\xff\xff\xff"
sequence_packet = 0x00

ssid_element_id = 0x00
ssid_element_length = 0x00

supported_rates_element_id = 0x01
supported_rates_length = 0x08
supported_rates = b''.join(bytes([rate]) for rate in [0x82, 0x84, 0x8b, 0x96, 0x24, 0x30, 0x48, 0x6c]) # Taxas (1, 2, 5.5, 11, 18, 24, 36, 54 Mbps

def send_packets_beacon(interface_network):
    # RADIOTAP IS THE STRUCTURE OF HEADERS FROM PACKETS, USEDS FOR GIVING INFORMATIONS IMPORTANTS ABOUT PACKETS, AS FREQUENCY,
    # DBM OF ANTENNA, CHANNEL ON WHICH IT WAS TRANSMITTED, FORCE OF THE SIGNAL, ETC...
    # WITH THE LIBRARY struct WE CAN CREATE PACKETS WITH DATA BYTES FOR BE SENT IN NETWORK.
    # AND THEN WE WILL WAIT FOR PACKETS OF RESPONSE, RECEIVED AND WITH THE struct UNPACK AND TRANSLATE THE DATA.

    # FORMING PACKET:
    # HEADER:
    header_radiotap = struct.pack('<BBHI', radiotap_header_version, radiotap_header_length, radiotap_flags, radiotap_dummy_field)
    
    # HEADER MAC(CONTROL ACCESS MIDDLE) OWN ADDRESSES AND OTHER INFORMAÇÕES IMPORTANTS
    source_packet = 
    header_mac = struct.pack(('<HH6s6s6sH'), frame_control, duration, source_packet, destiny_packet, bssid, sequence_packet)

    # SSID INFORMATIONS:
    ssid_info = struct.pack('<BB', ssid_element_id, ssid_element_length)
    
    # RATES SUPPORTEDS:
    rates_velocity = struct.pack('<BB', supported_rates_element_id, supported_rates_length) + supported_rates

    packet_beacon = header_radiotap + header_mac + ssid_info + rates_velocity

    socket_send = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
    socket_send.bind(('wlan0', 0))
    socket_send.send(packet_beacon)

interface = input("Type it Interface of Network: ")
send_packets_beacon(interface)
