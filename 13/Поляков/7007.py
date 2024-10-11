from ipaddress import *
n = ip_network('117.32.0.0/255.224.0.0')
k = 0
for i in n:
    s = f'{i:b}'
    ms = set([s[:8], s[8:16], s[16:24], s[24:]])
    if len(ms) == 3:
        k += 1
print(k - 2)