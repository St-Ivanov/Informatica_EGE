def f(x, y, f1):
    if x == y:
        return f1
    if x < y or x == 28:
        return 0
    if x == 20:
        f1 = 1
    return f(x - 3, y, f1) + f(x // 3, y, f1) + f(x // 2, y, f1)
print(f(46, 3, 0))