with open('17/17-408.txt') as f:
    sp = [int(i) for i in f.readlines()]

ans = []
mx = max(i for i in sp if abs(i) % 10 == 3 and len(str(i)) == 3)
for i in range(len(sp) - 2):
    x, y, z = sp[i], sp[i + 1], sp[i + 2]
    if ((abs(x) % 10 == 3 and len(str(abs(x))) == 3) + ((abs(y) % 10 == 3 and len(str(abs(y))) == 3)) + (abs(z) % 10 == 3 and len(str(abs(z))) == 3)) >= 1 and x + y + z < mx:
        ans.append(x + y + z)
print(len(ans), max(ans))
