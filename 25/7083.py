from itertools import product


B = []
for x in range(1, 5):
    for i in product('13579', repeat=x):
        B.append(int(''.join(i)))
for a in '02468':
    for b in B:
        num = int(f'1{a}2157{b}4')
        if num % 133 == 0 and num < 10 ** 10:
            print(num, num // 133)