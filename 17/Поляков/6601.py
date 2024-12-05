with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\17\Поляков\17-376.txt') as f:
    sp = [int(i) for i in f.readlines()]
mx = max([i for i in sp if (hex(i)[2:])[-2:] == '0f'])
ans = []
for i in range(len(sp) - 1):
    x, y = sp[i], sp[i + 1]
    if ((x % 7 == 0) + (y % 7 == 0)) == 1 and (x + y) % mx == 0:
        ans.append(x + y)
print(len(ans), min(ans))