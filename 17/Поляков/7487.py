with open('17/17-403.txt') as f:
    sp = [int(i) for i in f.readlines()]

mn = min(sp) ** 2
ans = []

for i in range(len(sp) - 1):
    x = sp[i]
    y = sp[i + 1]
    if (x % 77) * (y % 77) == mn:
        ans.append(x * y)

print(len(ans), min(ans))