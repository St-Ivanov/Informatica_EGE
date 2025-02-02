from itertools import product
ans = []
for A in '02468':
    for len in range(0, 4):
        for B in product('13579', repeat=len):
            B = ''.join(B)
            s = int(f'1{A}2157{B}4')
            if s <= 10 ** 10 and s % 133 == 0:
                ans.append([s, s // 133])
ans.sort()
for x, y in ans:
    print(x, y)