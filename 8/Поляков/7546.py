from itertools import product

kol = 0

for i in product('0123456789ABCD', repeat=5):
    if i[0] != '0' and i.count('9') == 1 and (i.count('B') + i.count('C') + i.count('D') <= 3):
        kol += 1
print(kol)