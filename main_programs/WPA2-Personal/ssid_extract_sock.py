import struct
import socket

def bytes_to_mac(mac_bytes):
    return ':'.join(format(byte, '02x') for byte in mac_bytes)

def show_packet_hex(packet):
    return ' '.join(format(byte, '02x') for byte in packet) 

def bytes_for_hex(data):
    return ''.join(format(bytes, '02x') for bytes in data)

def valid_ssid(ssid):
    if len(ssid) == 0 or len(ssid) > 32:
       return False
    for char in ssid:
        # IF CONDITION (32 <= ord(char) <= 126) IS FALSE IS RETURN false
        if not (32 <= ord(char) <= 126):           
           return False
    return True

# FOR EACH ESPECIFY FRAME IS NEEDED HANDLE THE PACKET IN DIFFERENT WAY 
def dissec_packet(packet):
    packet_hex = bytes_for_hex(packet)
    length_packet = len(packet)
    frame_control = packet_hex[128:128+4]

    try:
       radiotap_length = int(packet_hex[8:10], 16)
    except ValueError:
           radiotap_length = None
    try:
       length_ssid = int(packet_hex[210:212], 16)
    except ValueError:
           length_ssid = None
    if length_ssid is not None:
       ssid = packet_hex[212:212+4+length_ssid*2]
    else:
        ssid = None

    if frame_control == '8000':
       packet_beacon = {
        "Length packet": length_packet,
        "Radiotap length": radiotap_length,
        "Frame Control": f"Management Beacon Packet {frame_control}",
        "Length ssid": length_ssid,
        "SSID": ssid
       }
       return packet_beacon
    elif frame_control == '5000':
         packet_probe = {
          "Length packet": length_packet,
          "Radiotap length": radiotap_length,
          "Frame Control": f"Management Probe Packet {frame_control}",
          "Length ssid": length_ssid,
          "SSID": ssid
         }
         return packet_probe
    elif frame_control == '8802':
         eapol_frame = f"Qos Data Eapol {hex(frame_control)}"
         return eapol_frame
   
def intercept_packet():
    try:
       with socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003)) as sock:
            sock.bind(('wlan0mon', 0))
            while True:
                  packet, address = sock.recvfrom(2048)
                  packet_found = dissec_packet(packet)
                  print(packet_found)
    except Exception as error:
           print(f"Socket error ); {error}")
           sock.close()

intercept_packet()
