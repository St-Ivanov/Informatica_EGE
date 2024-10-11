from ipaddress import *
n = ip_network('94.253.128.0/255.255.128.0')
count = 0
for i in n:
    if f'{i:b}'.count('1') % 6 != 0 and f'{i:b}'[-3:] == '101':
        count += 1
print(count)