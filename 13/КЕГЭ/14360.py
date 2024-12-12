from ipaddress import *
for A in range(33):
    net = ip_network(f'153.202.16.37/{A}', 0)
    if str(net.network_address) == '153.202.16.32':
        print(net.netmask)