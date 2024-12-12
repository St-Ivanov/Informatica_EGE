from ipaddress import *
net = ip_network('192.168.31.80/255.255.255.240')
mx = 0
for i in net:
    s = f'{i:b}'
    mx = max(mx, s.count('1'))
print(mx)