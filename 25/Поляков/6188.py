from fnmatch import fnmatch


def delitely(n):
    ret = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ret.append(i)
            if i != n // i:
                ret.append(n // i)
    return list(filter(lambda x: fnmatch(str(x),'2*5*'), ret))


for i in range(0, 10**6 + 1, 3131):
    sp = delitely(i)
    sp.sort()
    if len(sp) == 3:
        print(i, sp[-1])