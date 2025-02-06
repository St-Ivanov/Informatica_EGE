def f(x, h):
    if x <= 49:
        return h % 2 == 0
    elif h == 0:
        return 0
    else:
        ans = [f(x - 2, h - 1), f(x - 5, h - 1), f(x // 3, h - 1)]
        if h % 2 == 1:
            return any(ans)
        return all(ans)
print([i for i in range(50, 200) if f(i, 2)])
print([i for i in range(50, 200) if f(i, 3) and not f(i, 1)])
print([i for i in range(50, 200) if (f(i, 2) or f(i, 4)) and not f(i, 2)])
