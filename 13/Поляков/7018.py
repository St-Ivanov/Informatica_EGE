from ipaddress import *

for m in range(33):
    net = ip_network(f'151.168.147.193/{m}', 0)
    if str(net.network_address) == '151.168.147.128':
        print(m)