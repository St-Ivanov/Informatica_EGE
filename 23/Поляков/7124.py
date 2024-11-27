def f(x, y, f1):
    if x < y or x == 32:
        return 0
    if x == y:
        return f1
    if x == 39:
        f1 = 1
    return f(x // 4, y, f1) + f(x - 1, y, f1) + f(x - 5, y, f1)
print(f(43, 17, 0))