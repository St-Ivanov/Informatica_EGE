def f(x, y, h):
    if x + y >= 178:
        return h % 2 == 0
    elif h == 0:
        return 0
    else:
        if h % 2 == 0:
            return any([f(x + 4, y, h - 1), f(x, y + 3, h - 1), f(x * 2, y, h - 1), f(x, y * 3, h - 1)])
        else:
            return any([f(x + 4, y, h - 1), f(x, y + 3, h - 1), f(x * 2, y, h - 1), f(x, y * 3, h - 1)])
print([i for i in range(1, 157) if f(21, i, 2)][0])
def f(x, y, h):
    if x + y >= 178:
        return h % 2 == 0
    elif h == 0:
        return 0
    else:
        if h % 2 == 1:
            return any([f(x + 4, y, h - 1), f(x, y + 3, h - 1), f(x * 2, y, h - 1), f(x, y * 3, h - 1)])
        else:
            return all([f(x + 4, y, h - 1), f(x, y + 3, h - 1), f(x * 2, y, h - 1), f(x, y * 3, h - 1)])
print(sum([i for i in range(1, 157) if f(21, i, 3) and not f(21, i, 1)]))
from math import prod
print(prod([i for i in range(1, 157) if f(21, i, 5) and not f(21, i, 3) and not f(21, i, 1)]))