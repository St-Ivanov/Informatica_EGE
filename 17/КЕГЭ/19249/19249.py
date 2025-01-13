with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\17\КЕГЭ\19249\19249.txt') as f:
    sp = [int(i) for i in f.readlines()]
mx = max([i for i in sp if len(str(abs(i))) == 5 and abs(i) % 100 == 43])
ans = []
for i in range(len(sp) - 2):
    x, y, z = sp[i], sp[i + 1], sp[i + 2]
    if (x ** 2 + y ** 2 + z ** 2) <= mx ** 2:
        if ((abs(x) % 100 == 43 and len(str(abs(x))) == 5) + \
            (abs(y) % 100 == 43 and len(str(abs(y))) == 5) + \
            (abs(z) % 100 == 43 and len(str(abs(z))) == 5)) > 0:
            ans.append(x ** 2 + y ** 2 + z ** 2)
print(len(ans), min(ans))