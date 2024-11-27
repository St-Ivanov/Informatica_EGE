from ipaddress import *
for m in range(33):
    net = ip_network(f'120.216.74.153/{m}', 0)
    if str(net.network_address) == '120.216.0.0':
        k = 0
        for ip in net:
            k += 1
        break
print(k)