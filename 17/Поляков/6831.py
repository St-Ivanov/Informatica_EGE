with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\17\Поляков\17-384.txt') as f:
    sp = [int(i) for i in f.readlines()]
mx = 0
for i in range(len(sp) - 1):
    x, y = sp[i], sp[i + 1]
    if len(str(x)) == 2 or len(str(y)) == 2:
        mx = max(mx, x + y)
ans = [i for i in sp if i > mx]
print(len(ans), min(ans))