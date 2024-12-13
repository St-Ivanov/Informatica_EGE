def delitely(n):
    ret = []
    for i in range(2, int(n * 0.5) + 1):
        if n % i == 0:
            ret.append(i)
            if n // i != i:
                ret.append(n // i)
    return list(set(ret))
def f(x, h, f1):
    if x >= 43:
        return h % 2 == 0
    elif h == 0:
        return 0
    else:
        if h % 2 == 0:
            if f1:
                ans = [f(x + 1, h - 1, f1), f(x + 4, h - 1, f1), f(x + sum(delitely(x)), h - 1, 0)]
            else:
                ans = [f(x + 1, h - 1, f1), f(x + 4, h - 1, f1)]
            return any(ans)
        else:
            if f1:
                ans = [f(x + 1, h - 1, f1), f(x + 4, h - 1, f1), f(x + sum(delitely(x)), h - 1, 0)]
            else:
                ans = [f(x + 1, h - 1, f1), f(x + 4, h - 1, f1)]
            return any(ans)
print([i for i in range(1, 43) if f(i, 2, 1)])
def f(x, h, f1):
    if x >= 43:
        return h % 2 == 0
    elif h == 0:
        return 0
    else:
        if h % 2 == 0:
            if f1:
                ans = [f(x + 1, h - 1, f1), f(x + 4, h - 1, f1), f(x + sum(delitely(x)), h - 1, 0)]
            else:
                ans = [f(x + 1, h - 1, f1), f(x + 4, h - 1, f1)]
            return all(ans)
        else:
            if f1:
                ans = [f(x + 1, h - 1, f1), f(x + 4, h - 1, f1), f(x + sum(delitely(x)), h - 1, 0)]
            else:
                ans = [f(x + 1, h - 1, f1), f(x + 4, h - 1, f1)]
            return any(ans)
print([i for i in range(1, 43) if f(i, 3, True) and not f(i, 1, True)])
print(len([i for i in range(1, 43) if f(i, 1, True)]))

