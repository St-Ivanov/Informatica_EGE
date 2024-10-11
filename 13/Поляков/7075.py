from ipaddress import *
n = ip_network('192.168.32.160/255.255.255.240')
k = 0
for i in n:
    if f'{i:b}'.count('0') > 21:
        k += 1
print(k)