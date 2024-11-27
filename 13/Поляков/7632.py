from ipaddress import *

net = ip_network('172.16.168.0/255.255.248.0')
k = 0
for ip in net:
    n = f'{ip:b}'
    if n.count('1') % 5 != 0:
        k += 1
print(k)