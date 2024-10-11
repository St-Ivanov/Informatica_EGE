from ipaddress import *
ans = []
for A in range(256):
    n = ip_network(f'159.242.{A}.223/255.255.254.0', 0)
    f = True
    for i in n:
        s = f'{i:b}'
        left = s[:16]
        right = s[16:]
        if left.count('0') >= right.count('0'):
            f = False
            break
    if f:
        ans.append(A)
print(max(ans))