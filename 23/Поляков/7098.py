def f(x, y, f1, f2):
    if x < y:
        return 0
    if x == y:
        return any([f1, f2])
    if x == 23:
        f1 = False
    if x == 20:
        f2 = False
    return f(x - 3, y, f1, f2) + f(x - 1, y, f1, f2) + f(x - 4, y, f1, f2)
print(f(43, 17, 1, 1))