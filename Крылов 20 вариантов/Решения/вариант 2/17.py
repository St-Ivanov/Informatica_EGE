with open(r'Крылов 20 вариантов\Решения\вариант 2\17.txt') as f:
    sp = [int(i) for i in f.readlines()]
mn = min(sp)
ans = []
for i in range(len(sp) - 1):
    x, y = sp[i], sp[i + 1]
    if x % 30 == mn or y % 30 == mn:
        ans.append(x + y)
print(len(ans), min(ans))