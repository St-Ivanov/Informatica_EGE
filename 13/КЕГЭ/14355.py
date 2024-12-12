from ipaddress import *
for A in range(0, 256):
    try:
        net = ip_network(f'127.63.67.1/255.255.{A}.0', 0)
        f = True
        for i in net:
            s = f'{i:b}'
            if s[:16].count('1') < s[16:].count('1'):
                f = False
                break
        if f:
            print(A)
            break
    except:
        pass