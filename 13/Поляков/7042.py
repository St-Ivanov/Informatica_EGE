from ipaddress import *

Alist = []
for i in range(1, 256):
    s = ('00000000' + bin(i)[2:])[-8:]
    sp = [k for k in s]
    sp.sort(reverse=True)
    if s == ''.join(sp) and s.count('1') > 0:
        Alist.append(i)


for A in Alist:
    net = ip_network(f'108.8.190.123/255.255.{A}.0', 0)
    f = True
    for ip in net:
        n = f'{ip:b}'
        if n[:16].count('1') > n[16:].count('1'):
            f = False
            break
    if f:
        print(A)
        break