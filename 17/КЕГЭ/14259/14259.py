def f1(n):
    n = str(abs(n))
    return max([int(i) for i in n])
with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\17\КЕГЭ\14259\14259.txt') as f:
    sp = [int(i) for i in f.readlines()]
mx = sum([i for i in sp if abs(i) % 1000 == 111])
ans = []
for i in range(len(sp) - 2):
    x, y, z = sp[i], sp[i + 1], sp[i + 2]
    if x * y * z >= mx:
        if ((abs(x) % f1(x) == 0) + (abs(y) % f1(y) == 0) + (abs(z) % f1(z) == 0)) > 0:
            ans.append(x * y * z)
print(len(ans), min(ans))