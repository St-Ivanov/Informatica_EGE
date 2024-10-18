def f(start, end, flag1):
    if end > start:
        return 0
    if start == end:
        return flag1
    if start == 22:
        flag1 = 1
    return f(start // 3, end, flag1) + f(start - 1, end, flag1) + f(start - 5, end, flag1)
print(f(46, 5, 0))