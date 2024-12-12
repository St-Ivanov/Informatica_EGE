from ipaddress import *
net = ip_network('112.154.132.0/255.255.252.0')
f = True
last = ''
k = 0
for i in net:
    s = f'{i:b}'
    if s[:16].count('1') <= s[16:].count('0') and s[16:].count('0') % 2 == 1:
        if f == 1:
            print(s)
            f = False
        k += 1
        last = s
print(last)
print(k)