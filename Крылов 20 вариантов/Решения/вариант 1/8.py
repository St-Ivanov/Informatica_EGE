from itertools import product
count = 0
for i in product('012345', repeat=6):
    i = ''.join(i)
    if i[0] != '0':
        if '10' not in i and '30' not in i and '50' not in i and \
            '01' not in i and '03' not in i and '05' not in i:
            count += 1
print(count)