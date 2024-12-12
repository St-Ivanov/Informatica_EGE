def f(x, h):
    if x >= 50:
        if x <= 70:
            return h % 2 == 0
        else:
            return h % 2
    elif h == 0:
        return 0
    else:
        if h % 2 == 0:
            return any([f(x + 1, h - 1), f(x * 2, h - 1)])
        else:
            return any([f(x + 1, h - 1), f(x * 2, h - 1)])
print([i for i in range(1, 50) if f(i, 2)])
def f(x, h):
    if x >= 50:
        if x <= 70:
            return h % 2 == 0
        else:
            return h % 2
    elif h == 0:
        return 0
    else:
        if h % 2 == 0:
            return all([f(x + 1, h - 1), f(x * 2, h - 1)])
        else:
            return any([f(x + 1, h - 1), f(x * 2, h - 1)])
print([i for i in range(1, 50) if not f(i, 1) and f(i, 3)])
print([i for i in range(1, 50) if f(i, 4) and not f(i, 2)])
