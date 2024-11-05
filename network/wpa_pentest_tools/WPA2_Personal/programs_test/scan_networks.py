import wifi

iface = input("Type it interface for operation: ")

def scan(interface):
    infos = wifi.Cell.all(interface)
    for info in infos:
        print(info)
scan(iface)
