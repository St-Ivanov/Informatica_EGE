def f(x, y, f1):
    if x == 11:
        f1 = 1
    if x == y:
        return f1
    elif x < y:
        return 0
    else:
        return f(x - 2, y, f1) + f(x // 2, y, f1)
print(f(50, 2, 0))