import struct

iface = struct.pack("H", 4)
nl80211_nlattr_iface = struct.pack("HH", struct.calcsize("HH") + len(iface), 3) + iface
nl80211_nlattr_max_ssids = struct.pack("HH", struct.calcsize("HH"), 0x2d)
nl80211_nlattr_scan_flags = struct.pack("HH", struct.calcsize("HH"), 0x9e)
nl80211_nlattrs = [nl80211_nlattr_iface, nl80211_nlattr_max_ssids, nl80211_nlattr_scan_flags]

print(struct.unpack("H", b"\x04\x00\x01\x00"))
