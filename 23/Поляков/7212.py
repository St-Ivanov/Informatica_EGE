def f(x, y, h, c):
    if x > y + 3 or abs(x) % 10 == 1:
        return 0
    if x == y:
        return h
    if x == 26:
        h = True
    if c != 'A' and c != 'B':
        return f(x - 1, y, h, 'A') + f(x - 3, y, h, 'B') + f(x + 6, y, h, 'C') + f(x * 3, y, h, 'D')
    return f(x + 6, y, h, 'C') + f(x * 3, y, h, 'D')

print(f(5, 58, 0, ''))