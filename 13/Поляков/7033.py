from ipaddress import *
n = ip_network('204.252.0.0/255.255.0.0')
mx = 0
for i in n:
    mx = max(mx, f'{i:b}'.count('1'))
print(mx)