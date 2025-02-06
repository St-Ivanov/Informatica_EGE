with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\Крылов 20 вариантов\Решения\вариант 1\17.txt') as f:
    sp = [int(i) for i in f.readlines()]
mn = min(sp)
ans = []
for i in range(len(sp) - 1):
    x, y = sp[i], sp[i + 1]
    if (x % 27 == mn or y % 27 == mn):
        ans.append(x + y)
print(len(ans), max(ans))