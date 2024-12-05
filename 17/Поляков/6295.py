with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\17\Поляков\17-354.txt') as f:
    sp = [int(i) for i in f.readlines()]
sr = [i for i in sp if len(str(i)) > 1 and str(i)[-1] == str(i)[-2]]
sr = sum(sr) / len(sr)
ans = []
for i in range(len(sp) - 1):
    x, y = sp[i], sp[i + 1]
    if len(str(abs(x))) > 1 and len(str(abs(y))) > 1:
        if str(x)[-1] == str(y)[-2] or str(x)[-2] == str(y)[-1]:
            if ((abs(x) % 11 == 0) + (abs(y) % 11 == 0)) == 1:
                if (x ** 2 + y ** 2) >= sr ** 2:
                    ans.append(x ** 2 + y ** 2)
print(len(ans), max(ans))