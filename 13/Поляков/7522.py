from ipaddress import *
net = ip_network('112.160.0.0/255.240.0.0')
k = 0
for i in net:
    if f'{i:b}'.count('1') % 3 != 0:
        k += 1
print(k)