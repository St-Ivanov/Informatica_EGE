def f(x, y, f1, f2):
    if x > y or x == 15 or x == 30:
        return 0
    if x == y:
        return f1 * f2
    if x == 10:
        f1 = 1
    if x == 20:
        f2 = 1
    return f(x + 2, y, f1, f2) + f(x + 3, y, f1, f2) + f(x ** 2, y, f1, f2)
print(f(3, 38, 0, 0))