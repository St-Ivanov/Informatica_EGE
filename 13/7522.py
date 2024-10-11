from ipaddress import *


net = ip_network('112.160.0.0/255.240.0.0')
print(net)
print(bin(112)[2:] + ' ' + bin(160)[2:])


from itertools import product


k = 0
for i in product('01', repeat=20):
    if (i.count('1') + 5) % 3 != 0:
        k += 1
print(k)