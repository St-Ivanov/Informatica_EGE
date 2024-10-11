with open('17/17-407.txt') as f:
    sp = [int(i) for i in f.readlines()]

mx = len([i for i in sp if abs(i) % 32 == 0])

ans = []

for i in range(len(sp) - 1):
    x, y = sp[i], sp[i + 1]
    if (x < 0 or y < 0) and (x + y) < mx:
        ans.append(x + y)
print(len(ans), max(ans))
