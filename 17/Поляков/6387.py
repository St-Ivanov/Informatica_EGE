with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\17\Поляков\17-369.txt') as f:
    sp = [int(x) for x in f.readlines()]
def ub(n):
    s = str(n)
    for i in range(len(s) - 1):
        if int(s[i]) <= int(s[i + 1]):
            return False
    return True
def voz(n):
    s = str(n)
    for i in range(len(s) - 1):
        if int(s[i]) >= int(s[i + 1]):
            return False
    return True
mn = min([i for i in sp if ub(i)])
mn = sum([int(i) for i in str(mn)])
ans = []
for i in range(len(sp) - 1):
    x, y = sp[i], sp[i + 1]
    if ((voz(x)) + (voz(y))) == 1 and (x * y) % mn == 0:
        ans.append(x + y)
print(len(ans), min(ans))