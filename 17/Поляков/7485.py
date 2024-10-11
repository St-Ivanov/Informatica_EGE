with open('17/17-404.txt') as f:
    sp = [int(i) for i in f.readlines()]


ans = []
mn = min(sp)
for i in range(len(sp) - 1):
    x, y = sp[i], sp[i + 1]
    if x % 55 == mn or y % 55 == mn:
        ans.append(x + y)
print(len(ans), min(ans))