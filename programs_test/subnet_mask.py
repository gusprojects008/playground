def split_ip():
    subnet_mask = '255.255.255.0'
    subnet_mask_split = subnet_mask.split('.')
    subnet_bin = [bin(int(octet))[2:].zfill(8) for octet in subnet_mask_split]
    subnet_join_bin = ''.join(subnet_bin).count('1')
    cidr_value = subnet_join_bin.count('1')
    print(subnet_join_bin)

#    subnet_mask_join = ''.join(subnet_mask_split)
split_ip()
