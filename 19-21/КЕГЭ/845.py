def f(x, h):
    if x >= 36:
        if x < 60:
            return h % 2 == 0
        return h % 2 == 1
    elif h == 0:
        return 0
    else:
        ans = [f(x + 1, h - 1), f(x * 2, h - 1), f(x * 3, h - 1)]
        if h % 2 == 1:
            return any(ans)
        else:
            return all(ans)
print(min([i for i in range(1, 36) if f(i, 2)]))
def f(x, h):
    if x >= 36:
        if x < 60:
            return h % 2 == 0
        return h % 2 == 1
    elif h == 0:
        return 0
    else:
        ans = [f(x + 1, h - 1), f(x * 2, h - 1), f(x * 3, h - 1)]
        if h % 2 == 1:
            return any(ans)
        else:
            return all(ans)
print(len([i for i in range(1, 36) if f(i, 3) and not f(i, 1)]))
def f(x, h):
    if x >= 36:
        if x < 60:
            return h % 2 == 0
        return h % 2 == 1
    elif h == 0:
        return 0
    else:
        ans = [f(x + 1, h - 1), f(x * 2, h - 1), f(x * 3, h - 1)]
        if h % 2 == 1:
            return any(ans)
        else:
            return all(ans)
print(([i for i in range(1, 36) if (f(i, 4) or f(i, 2)) and not f(i, 2)]))