from ipaddress import *

for m in range(33):
    net1 = ip_network(f'154.63.206.129/{m}', 0)
    net2 = ip_network(f'154.63.100.75/{m}', 0)
    if net1 != net2:
        print(net1.netmask)