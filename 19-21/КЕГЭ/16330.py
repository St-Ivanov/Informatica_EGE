def f(x, y, h):
    if x + y >= 59:
        return h % 2 == 0
    elif h == 0:
        return 0
    else:
        ans = [f(x + 1, y, h - 1), f(x * 2, y, h - 1), f(x, y + 1, h - 1), f(x, y * 2, h - 1)]
        if h % 2 == 0:
            return any(ans)
        else:
            return any(ans)
print([i for i in range(1, 54) if f(5, i, 2) and (not f(5, i, 1))])
def f(x, y, h):
    if x + y >= 59:
        return h % 2 == 0
    elif h == 0:
        return 0
    else:
        ans = [f(x + 1, y, h - 1), f(x * 2, y, h - 1), f(x, y + 1, h - 1), f(x, y * 2, h - 1)]
        if h % 2 == 0:
            return all(ans)
        else:
            return any(ans)
print([i for i in range(1, 54) if f(5, i, 3) and (not f(5, i, 1))])
print([i for i in range(1, 54) if (f(5, i, 4) or f(5, i, 2)) and (not f(5, i, 2))])
