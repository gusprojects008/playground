import socket
import struct

interface = input("Type it interface Network to operation: ")

def identify_type_packet(packets):
    # THE VALUE OF FRAME CONTROL IS 16 BITS WITH INFORMATION FRAME CONTROL, THEN IS NEEDED THAT DO OPERATIONS
    # BIT TO BIT FOR EXTRACT ALL REQUIRED INFORMATION
    packet_frame_control = struct.unpack("<H", packets[:2])[0]
    frame_type = (packet_frame_control >> 2) & 0x03
    frame_subtype = (packet_frame_control >> 4) & 0x0F

    if frame_type == 0:
       if frame_subtype == 8:
          return "Packet Beacon"
       elif frame_subtype == 5:
            return "Packet Probe Response"

       elif frame_subtype == 0:
            return "Association Request"
       elif frame_subtype == 1:
            return "Association Response"
       elif frame_subtype == 2:
            return "Reassociation Request"
       elif frame_subtype == 3:
            return "Reassociation Response"

       elif frame_subtype == 12:
            return "Deauthentication Packet"
       elif frame_subtype == 11:
            return "Authentication Packet"

       elif frame_subtype == 10:
            return "Disassociation Packet"
       return None

def extract_ssid(packets):
    # THE SSID GENERALLY START FROM 36 BYTES
    ssid_position = packets[36]
    packet_length = len(packets)

    while ssid_position < packet_length:
          tag_number = packets[ssid_position]
          tag_length = packets[ssid_position + 1]
          
          if tag_number == 0:
             ssid = packets[ssid_position+2:ssid_position+2+tag_length]
             if tag_length == 0:
                return "Hidden SSID );"
             else:
                 return ssid.decode("utf-8", errors="ignore")
          ssid_position += 2 + tag_length
    return "SSID Not Found );"
    
def bytes_to_mac(mac_bytes):
    return ':'.join(format(byte, 'x') for byte in mac_bytes)

def decode_packets(packet, address):
    return f"SSID: {extract_ssid(packet)} FRAME TYPE: {identify_type_packet(packet)} MAC ORIGIN: {bytes_to_mac(packet[10:16])}"

def send_packets(interface):
    packet_deauthentication = struct.pack("<HHH6s6s", 0x00, 0x00, 0x00, b'\xff\xff\xff\xff\xff\xff', b'\x00\x00\x00\x00\x00\x00')
    with socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x003)) as sock:
         sock.bind((interface, 0))
         sock.send(packet_deauthentication)
         while True:
               packet, address = sock.recvfrom(2048)
               if identify_type_packet(packet):
                  print(decode_packets(packet, address))

#send_packets(interface)

def capture_packets(interface):
    with socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x003)) as sock:
         sock.bind((interface, 0))
         while True:
               packet, address = sock.recvfrom(2000)
               if identify_type_packet(packet):
                  print(decode_packets(packet, address))
                  print(f"Data packet hex: {packet.hex()}")
                  print(f"Data packet repr: {repr(packet)}")
                  print()
          
send_packets(interface)
