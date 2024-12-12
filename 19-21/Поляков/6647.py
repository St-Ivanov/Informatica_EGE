# а
def f(x, y, h):
    if x * y >= 123:
        return h % 2 == 0
    elif h == 0:
        return 0
    else:
        if h % 2 != 1:
            return any([f(x + 2, y, h - 1), f(x * 2, y, h - 1), f(x, y + 2, h - 1), f(x, y * 2, h - 1)])
        else:
            return any([f(x + 2, y, h - 1), f(x * 2, y, h - 1), f(x, y + 2, h - 1), f(x, y * 2, h - 1)])
print([i for i in range(1, 41) if f(3, i, 2)][-1])

# б в
def f(x, y, h):
    if x * y >= 123:
        return h % 2 == 0
    elif h == 0:
        return 0
    else:
        if h % 2 != 1:
            return all([f(x + 2, y, h - 1), f(x * 2, y, h - 1), f(x, y + 2, h - 1), f(x, y * 2, h - 1)])
        else:
            return any([f(x + 2, y, h - 1), f(x * 2, y, h - 1), f(x, y + 2, h - 1), f(x, y * 2, h - 1)])
print([i for i in range(1, 41) if not f(3, i, 1) and f(3, i, 3)][-2:])
print([i for i in range(1, 41) if not f(3, i, 2) and f(3, i, 4)][-1])