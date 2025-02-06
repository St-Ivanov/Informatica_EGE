def f(x, y, f1):
    if x == 14:
        f1 = 1
    if x < y:
        return 0
    elif x == y:
        return f1
    else:
        return f(x - 2, y, f1) + f(x // 2, y, f1)
print(f(52, 2, 0))