def ff(x, y, f):
    if x == y:
        return f
    if x == 16:
        f = True
    if x < y:
        return 0
    return ff(x - 2, y, f) + ff(x // 2, y, f)
print(ff(38, 2, False))