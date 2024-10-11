from ipaddress import *
for mask in range(33):
    net = ip_network(f'203.155.196.98/{mask}', 0)
    if str(net)[:-3] == '203.155.192.0':
        print(mask)
