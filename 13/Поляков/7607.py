from ipaddress import *

net = ip_network('94.149.96.0/255.255.224.0')

k = 0
for ip in net:
    n = f'{ip:b}'
    if n.count('1') % 3 == 0 and n[-2:] == '11':
        k += 1
print(k)