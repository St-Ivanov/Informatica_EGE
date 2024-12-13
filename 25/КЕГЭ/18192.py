def delitely(n):
    ret = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            ret.append(i)
            if n // i != i:
                ret.append(n // i)
    ret = list(set(ret))
    return ret
def prost(a):
    ret = []
    for i in a:
        if len(delitely(i)) == 0:
            ret.append(i)
    return ret
k = 0
for i in range(10 ** 6, 10 ** 7):
    s = prost(delitely(i))
    s.sort()
    if len(s) == 3:
        print(i, s[-1])
        k += 1
    if k == 5:
        break