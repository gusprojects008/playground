import struct

supported_rates = b''.join(bytes([rate]) for rate in [0x82, 0x84, 0x8b, 0x96, 0x24, 0x30, 0x48, 0x6c])

print(supported_rates, '\n')

print(struct.unpack('B'*8, supported_rates))
