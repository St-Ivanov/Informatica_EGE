def delitely(n):
    ret = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            ret.append(i)
            if i != n // i:
                ret.append(n // i)
    return ret


ans = []
count = 0
for i in range(800000 - 1, 0, -1):
    delitely_sp = delitely(i)
    if len(delitely_sp) >= 2:
        delitely_sp.sort()
        M = delitely_sp[0] + delitely_sp[-1]
        if M % 10 == 2:
            ans.append((i, M))
            count += 1
        if count == 5:
            break
print(ans[::-1])
