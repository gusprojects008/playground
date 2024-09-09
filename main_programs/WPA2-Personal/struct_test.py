import struct

little_endian_val = struct.pack('<h', 1234)
big_endian_val = struct.pack('>h', 1234)

print(f"LITTLE ENDIAN: {struct.unpack('<h', little_endian_val)}\nBIG ENDIAN: {struct.unpack('>h', big_endian_val)}")
