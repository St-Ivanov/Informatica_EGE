from ipaddress import *

net = ip_network('140.19.96.0/255.255.248.0')
k = 0
for ip in net:
    n = f'{ip:b}'
    if n[:8].count('1') == n[8:16].count('1') == n[16:24].count('1') == n[24:].count('1'):
        k += 1
print(k)