from ipaddress import *

for mask in range(33):
    net = ip_network(f'113.191.169.34/{mask}', 0)
    print(net, net.netmask)
 