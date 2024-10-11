from ipaddress import *


net = ip_network(f'115.198.0.0/255.254.0.0')
print(net)
print(bin(115)[2:] + ' ' + bin(198)[2:])

from itertools import product


k = 0
for i in product('01', repeat=17):
    if (i.count('1') + 9) % 5 == 0:
        k += 1
print(k)