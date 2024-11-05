from pyroute2 import IPRoute

ip = IPRoute()
links = ip.get_links()

for link in links:
    print(link)
