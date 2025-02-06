from itertools import product
count = 0
block = ['0' + i for i in '2468'] + [i + '0' for i in '2468']
for i in product('0123456', repeat=6):
    i = ''.join(i)
    if i[0] != '0' and i.count('0') == 1:
        f = True
        for k in block:
            if k in i:
                f = False
                break
        if f:
            count += 1
print(count)