from ipaddress import *
net = ip_network(f'115.198.0.0/255.254.0.0')
count = 0
for i in net:
    if f'{i:b}'.count('1') % 5 == 0:
        count += 1
print(count)