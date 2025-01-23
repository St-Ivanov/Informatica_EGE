def f(x, h):
    if x >= 50:
        return h % 2 == 0
    elif h == 0:
        return 0
    else:
        if x * 3 <= 119:
            ans = [f(x + 2, h - 1), f(x * 3, h - 1)]
        else:
            ans = [f(x + 2, h - 1)]
        if h % 2 == 0:
            return any(ans)
        else:
            return all(ans)
print(len([i for i in range(1, 50) if f(i, 2)]))
def f(x, h):
    if x >= 50:
        return h % 2 == 0
    elif h == 0:
        return 0
    else:
        if x * 3 <= 119:
            ans = [f(x + 2, h - 1), f(x * 3, h - 1)]
        else:
            ans = [f(x + 2, h - 1)]
        if h % 2 == 0:
            return all(ans)
        else:
            return any(ans)
print(min([i for i in range(1, 50) if f(i, 3) and not f(i, 0)]))
def f(x, h):
    if x >= 50:
        if x > 199:
            return h % 2 == 1
        return h % 2 == 0
    elif h == 0:
        return 0
    else:
        if x * 3 <= 119:
            ans = [f(x + 2, h - 1), f(x * 3, h - 1)]
        else:
            ans = [f(x + 2, h - 1)]
        if h % 2 == 0:
            return all(ans)
        else:
            return any(ans)
print(([i for i in range(1, 50) if (f(i, 4) or f(i, 2)) and not f(i, 2)]))