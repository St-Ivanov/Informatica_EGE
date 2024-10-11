def delitely(n):
    ret = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            ret.append(i)
            if i != n // i:
                ret.append(n // i)
    return ret


count = 0
for i in range(600001, 1000000):
    sp = delitely(i)
    sp.sort()
    sp = list(filter(lambda x: x % 10 == 7 and x != 7, sp))
    if len(sp) > 0:
        print(i, sp[0])
        count += 1
    if count == 5:
        break
