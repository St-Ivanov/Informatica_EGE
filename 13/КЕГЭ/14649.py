from ipaddress import *
for A in range(255, 0, -1):
    net = ip_network(f'116.242.{A}.26/255.255.255.224', 0)
    t = True
    for ip in net:
        s = f'{ip:b}'
        if s[:16].count('1') < s[16:].count('1'):
            t = False
            break
    if t:
        print(A)
        break