def delitely(n):
    ret = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ret.append(i)
            if i != n // i:
                ret.append(n // i)
    return ret

for i in range(100000 + 1):
    for k in '123456789':
        num = int(str(k) * 2 + str(i) + str(k) * 2)
        sp = delitely(num)
        sp.sort()
        if len(sp) == 117:
            print(num, sp[-2])
