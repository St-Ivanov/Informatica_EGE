with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\17\КЕГЭ\9840\9840.txt') as f:
    sp = [int(i) for i in f.readlines()]
mx = max([i for i in sp if len(str(abs(i))) == 4 and abs(i) % 100 == 39])
ans = []
for i in range(len(sp) - 1):
    x, y = sp[i], sp[i + 1]
    if ((len(str(abs(x))) == 4) + (len(str(abs(y))) == 4)) == 1 and (x + y) ** 2 <= mx ** 2:
        ans.append(x + y)
print(len(ans), max(ans))