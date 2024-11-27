def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(int('2' + str(x)), y)
print(f(3, 678))