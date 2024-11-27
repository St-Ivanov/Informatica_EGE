def delitely(n):
    ret = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            ret.append(i)
            if n // i != i:
                ret.append(n // i)
    ret.sort()
    return ret

k = 0
ans = []
for i in range(900000, 0, -1):
    de = delitely(i)
    if len(de) > 0:
        M = de[0] + de[-1]
    else:
        M = 0
    if M % 1000 == 112:
        ans.append((i, M))
        k += 1
    if k == 5:
        break
ans.sort()
for i in ans:
    print(i)