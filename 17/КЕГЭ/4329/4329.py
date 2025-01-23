def delitely(n):
    ret = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ret.add(i)
            if i != n // i:
                ret.add(n // i)
    return ret

with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\17\КЕГЭ\4329\4329.txt') as f:
    sp = [int(i) for i in f.readlines()]
mx_del = max([delitely(i) for i in sp], key=len)
ans = []
for i in range(len(sp) - 1):
    x, y = sp[i], sp[i + 1]
    del_x = delitely(x)
    del_y = delitely(y)
    if len(del_x & mx_del) >= 3 and len(del_y & mx_del) >= 3:
        ans.append(len(del_x & del_y))
print(len(ans), max(ans))
