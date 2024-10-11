from ipaddress import *

for mask in range(33):
    net = ip_network(f'93.138.70.47/{mask}', 0)
    print(net)