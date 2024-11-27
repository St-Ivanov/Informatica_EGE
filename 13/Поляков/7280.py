from ipaddress import *

for mask in range(33):
    net1 = ip_network(f'176.213.225.119/{mask}', 0)
    net2 = ip_network(f'176.213.195.58/{mask}', 0)
    if net1 == net2:
        print(net1.netmask)
