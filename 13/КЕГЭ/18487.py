from ipaddress import *
for A in range(0, 256):
    net = ip_network(f'192.214.{A}.184/255.255.255.224', 0)
    t = True
    for ip in net:
        s = f'{ip:b}'
        if s.count('1') <= 15:
            t = False
            break
    if t:
        print(A)
        break