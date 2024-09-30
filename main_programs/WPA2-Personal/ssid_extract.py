import struct
import socket

packet_probe = bytes.fromhex("0000000038002f4040a0200800a0200800000010d1c2119ab3000000000c71164001b600002000000000000000002e197c1c00000000003016001103b600b10150000000a4f933ed00405b755c628b80838c5c628b80838cc0020050f1c2119ab300000064001118000a414e0060454c4953455f354701088c129824b0480070606c03019530140100000fac0401000000800fac040100000fac0200002d1aef01170090ffff000000000000000000000000000000a0000018048709003d169505040000000000b00000000000000000000000000000007f00c00800000800000000400b05020000127a00d0dd180050f2020101800003a4000027a400e0000042435e0062322f0046057200010000f0003305802a3a6a7a20010323023f00c3010004027e7e7e070a425220240423950523011000bf0cb179c933faff0c03faff0c03c0012005019b00faffdd7d0050f204104a00010130101044000102103b000103104700100001400000000000100000005c628b80838a10015021000754502d4c696e6b10230008454301603232302d473510240003332e30104200017007312e312e312e3310540008000600500180f20400011011000845433232302d4735019010080002228c103c000103104900060001a0372a000120dd07000c4303000000dd2101b0000ce700000000bf0cb101c0332aff9201c0042aff9204c0050000002affc303010201d002")
packet_random = bytes.fromhex("0000000036002f4040a020080000000000000010a215bb2cb800000000029909a000ce0000200000000000000000106cf9ae00000000003016001103ce0008620000ffffffffffff00405c628b80838a5c628b80838aa07f602b005000601b000000aaaa030000000806000100600800060400015c628b80838ac0a800010070000000000000c0a80008")
#packet_beacon = bytes.fromhex("0000000038002f4040a0200800a0200800000010137d0c9ab300000000026c09a000b70000200000000000000000bfd2761c00000000003016001103b300b70180000000ffffffff0040ffff50c7bf7ad45d50c7bf7ad45d40f60050dc814d580e0800006400110c000e52650060646d695f303333385f4558540108828400708b961224486c03010132040c183060330080082001020304050607330821050607080090090a0b050400010000dd1a0050f2010100a0000050f20202000050f2020050f2040100b0000050f20230180100000fac0202000000c00fac02000fac040100000fac0200002a00d001042d1aee1117ffff0000010000000000e000000000000000000000000000003d1600f00105000000000000000000000000000001000000000000004a0e14000a002c01c8000110140005001900dd180050f20201018600012003a4000027a4000042435e0062322f0001300b05000000127add07000c4303000000")
#packet_eapol = bytes.fromhex("0000000038002f4040a0200800a0200800000010b86604bfb600000000029909a000c900002000000000000000009235454100000000003016001103c900c7018802ca00a4f933ed00405b755c628b80838a5c628b80838a000000500000aaaa03000000888e01030075020000608a0010000000000000000127b15ea23200708d61802fdc99f65e8868dc09db4b05ca00807012058d76f0f94bbcfcd5000000000000900000000000000000000000000000000000a00000000000000000000000000000000000b000000000000000000000000016dd140000c00fac04b11ddc95c7c78d1e3fc6a72ed100d04afd3e")


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
        if not (32 <= ord(char) <= 126):           
           return False
    return True

#def dissec_packet(packet):

def capture_ssid(packet):
    packet_hex = bytes_for_hex(packet)
    length_packet = len(packet)
    if length_packet > 250:
       radiotap_length = int(packet_hex[8:10], 16)
       frame_control = packet_hex[128:128+4]
       try:
          length_ssid = int(packet_hex[210:212], 16)
          ssid = packet_hex[212:212+4+length_ssid]
       except ValueError:
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

    #packet_test = {
    # "Length packet": length_packet,
    # "Radiotap length": radiotap_length,
    # "Frame Control": f"Management Random Packet {frame_control}",
    # "Length ssid": length_ssid,
    # "SSID": ssid
    #}
    #return packet_test
def intercept_packet():
    try:
       with socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003)) as sock:
            sock.bind(('wlan0mon', 0))
            while True:
                  packet, address = sock.recvfrom(2048)
                  packet_found = capture_ssid(packet)
                  if packet_found:
                     print(packet_found)
    except Exception as error:
           print(f"Socket error ); {error}")
           sock.close()
#intercept_packet()
print(capture_ssid(packet_probe))
print()
print(capture_ssid(packet_random))
