def f(x, y, f1):
    if x == 10:
        f1 = 1
    if x == y:
        return f1
    if x < y:
        return 0
    return f(x - 2, y, f1) + f(x // 2, y, f1)
print(f(38, 2, 0))