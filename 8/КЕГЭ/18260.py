from itertools import product
k = 0
for i in product('0123456789AB', repeat=6):
    if i[0] != '0' and i.count('B') == 1:
        if (i.count('0') + i.count('2') + i.count('4') + i.count('6') + i.count('8') + i.count('A')) == \
        (i.count('1') + i.count('3') + i.count('5') + i.count('7') + i.count('9') + i.count('B')):
            k += 1
print(k)