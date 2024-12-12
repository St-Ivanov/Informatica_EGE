from ipaddress import *
for A in range(0, 256):
    net = ip_network(f'183.192.{A}.0/255.255.252.0', 0)
    f = True
    for i in net:
        s = f'{i:b}'
        if s[16:].count('1') <= 3:
            f = False
            break
    if f:
        print(A)
        break
