from itertools import product


k = 0
for i in product('0123456789ab', repeat=5):
    if i[0] != '0' and (i.count('a') + i.count('b') + i.count('9') <= 3) and i.count('7') == 1:
        k += 1
print(k)
