def f(x, y, h):
    if x == y:
        return (h == 'A' or h == 'C')
    elif x > y:
        return 0
    return f(x + 2, y, 'A') + f(x + 3, y, 'B') + f(x * 2, y, 'C')
print(f(3, 20, ''))