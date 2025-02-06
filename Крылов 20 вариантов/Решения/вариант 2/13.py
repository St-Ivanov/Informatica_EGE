from ipaddress import *
net = ip_network('200.33.100.0/255.255.248.0', 0)
count = 0
for ip in net:
    ip = f'{ip:b}'
    if ip.count('1') % 7 != 0:
        count += 1
print(count)