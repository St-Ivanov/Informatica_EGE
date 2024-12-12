def delitely(n):
    ret = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            ret.append(i)
            if n // i != i:
                ret.append(n // i)
    return ret

def f(x, h):
    if x >= 63:
        return h % 2 == 0
    elif h == 0:
        return 0
    else:
        sp = delitely(x)
        if len(sp) == 0:
            ans = [f(x + 1, h - 1)]
        else:
            ans = [f(x + i, h - 1) for i in sp]
        if h % 2 == 0:
            return all(ans)
        else:
            return any(ans)
print([i for i in range(1, 63) if f(i, 2)])
print([i for i in range(1, 63) if f(i, 3) and (not f(i, 1))])
print([i for i in range(1, 63) if (f(i, 4) or f(i, 2)) and (not f(i, 2))])

