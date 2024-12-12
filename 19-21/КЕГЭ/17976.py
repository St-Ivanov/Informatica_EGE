def f(x, h):
    if x <= 17:
        return h % 2== 0
    elif h == 0:
        return 0
    else:
        ans = [f(x - 3, h - 1), f(x - 5, h - 1), f(x // 2, h - 1)]
        if h % 2 == 0:
            return all(ans)
        else:
            return any(ans)
print([i for i in range(18, 100) if f(i, 2) and (not f(i, 1))])
print([i for i in range(18, 100) if f(i, 3) and (not f(i, 1))])
print([i for i in range(18, 100) if (f(i, 4) or f(i, 2) and f(i, 2))])
