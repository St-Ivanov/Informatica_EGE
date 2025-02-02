from ipaddress import *
net = ip_network('204.16.168.0/255.255.248.0', 0)
count = 0
for ip in net:
    s = f'{ip:b}'
    if s.count('1') % 5 != 0:
        count += 1
print(count)