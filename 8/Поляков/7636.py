from itertools import product

k = 0
for i in product('0123456789AB', repeat=5):
    if i[0] != '0' and i.count('7') == 1 and (i.count('9') + i.count('A') + i.count('B')) <= 3:
        k += 1
print(k)