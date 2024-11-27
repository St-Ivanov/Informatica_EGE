def f(x, y, c):
    if x > y:
        return 0
    if x == y:
        return 1
    if c == 'A':
        return f(x + 3, y, 'A') + f(x * 7, y, 'C')

    return f(x + 3, y, 'A') + f(x * 5, y, 'B') + f(x * 7, y, 'C')
print(f(1, 1000, ''))