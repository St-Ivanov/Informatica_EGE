def f(x, y, h):
    if x == y:
        return h
    if x == 7:
        h = True
    if x > y:
        return 0
    return f(x + 1, y, h) + f(x + 2, y, h) + f(x + 3, y, h)
print(f(5, 11, 0))