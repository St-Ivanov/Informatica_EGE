def f(x, y, h):
    if x == y:
        return h <= 2
    if x > y or h > 2:
        return 0
    return f(x - 2, y, h + 1) + f(x * 2, y, h) + f(x * 3, y, h)
print(f(6, 48, 0))