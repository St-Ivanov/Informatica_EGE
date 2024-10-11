with open('17/17-409.txt') as f:
    sp = [int(i) for i in f.readlines()]

ans = []

mx = max([i for i in sp if len(str(abs(i))) == 4 and i % 10 == 7])
for i in range(len(sp) - 2):
    x, y, z = sp[i], sp[i + 1], sp[i + 2]
    if (bool(abs(x) % 10 == 7 and len(str(abs(x))) == 4) + bool(abs(y) % 10 == 7 and len(str(abs(y))) == 4) + bool(abs(z) % 10 == 7 and len(str(abs(z))) == 4)) >= 2 and (x + y + z) > mx:
        ans.append(x + y + z)
print(len(ans), max(ans))
