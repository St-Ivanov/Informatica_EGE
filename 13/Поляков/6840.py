from ipaddress import *
n = ip_network('192.168.248.176/255.255.255.240')
k = 0
for i in n:
    s = f'{i:b}'
    if s.count('1') == s.count('0'):
        k += 1
print(k)