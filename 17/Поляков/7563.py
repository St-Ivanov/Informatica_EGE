with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\17\Поляков\17-408.txt') as f:
    sp = [int(i) for i in f.readlines()]


mx = max(list(filter(lambda x: abs(x) % 10 == 3 and len(str(abs(x))) == 3, sp)))
ans = []
for i in range(len(sp) - 2):
    x, y, z = sp[i], sp[i + 1], sp[i + 2]
    if ((len(str(abs(x))) == 3 and abs(x) % 10 == 3) + \
        (len(str(abs(y))) == 3 and abs(y) % 10 == 3) + \
        (len(str(abs(z))) == 3 and abs(z) % 10 == 3)) > 0:
        if x + y + z < mx:
            ans.append(x + y + z)
print(len(ans), max(ans))