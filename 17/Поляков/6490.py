with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\17\Поляков\17-370.txt') as f:
    sp = [int(i) for i in f.readlines()]
def palindrom_3(n):
    s = ''
    while n != 0:
        s += str(n % 3)
        n //= 3
    return s == s[::-1]
ans = []
mx = max([x for x in sp if len(str(abs(x))) == 3 and palindrom_3(abs(x))])
for i in range(len(sp) - 1):
    x, y = sp[i], sp[i + 1]
    if ((len(str(abs(x))) == 4) + (len(str(abs(y))) == 4)) == 1 and (x ** 2 + y ** 2) % mx == 0:
        ans.append(x ** 2 + y ** 2)
print(len(ans), min(ans))