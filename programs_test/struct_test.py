import struct

pack_struct = struct.pack('ccHB', b'1', b'a', 2, 2)
print(pack_struct)
