with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\17\Поляков\17-388.txt') as f:
    sp = [int(i) for i in f.readlines()]


mx = max([i for i in sp if abs(i) % 100 == 68])
ans = []
for i in range(len(sp) - 3):
    x, y, w, z = sp[i], sp[i + 1], sp[i + 2], sp[i + 3]
    two = (len(str(abs(x))) == 2) + (len(str(abs(y))) == 2) + (len(str(abs(w))) == 2) + (len(str(abs(z))) == 2)
    if (two == 1 or two == 4) and (x + y + w + z) >= mx:
        ans.append(x + y + w + z)
print(len(ans), max(ans))