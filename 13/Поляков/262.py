from ipaddress import *

for m in range(0, 33):
    net1 = ip_network(f'121.171.15.70/{m}', 0)
    net2 = ip_network(f'121.171.3.68/{m}', 0)
    if net1 == net2:
        print(net1.netmask)
