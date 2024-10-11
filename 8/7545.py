from itertools import product


kol = 0

for i in product('0123456789ABCDE', repeat=5):
    if i[0] != '0' and i.count('8') == 1 and (i.count('A') + i.count('B') + i.count('C') + i.count('D') + i.count('E') >= 2):
        kol += 1
print(kol)
