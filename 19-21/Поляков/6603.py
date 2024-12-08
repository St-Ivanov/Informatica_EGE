# а
def f(x, h):
    if x == 0:
        return h % 2 == 0
    elif h == 0:
        return 0
    else:
        if h % 2 == 0:
            if x - 5 >= 0:
                return all([f(x - 5, h - 1), f(x // 3, h - 1)])
            else:
                return all([f(x // 3, h - 1)])
        else:
            if x - 5 >= 0:
                return any([f(x - 5, h - 1), f(x // 3, h - 1)])
            else:
                return any([f(x // 3, h - 1)])
print([i for i in range(0, 1000) if f(i, 2)])
print([i for i in range(0, 1000) if f(i, 3) and not f(i, 1)])
print([i for i in range(0, 1000) if f(i, 4) and not f(i, 2)])
