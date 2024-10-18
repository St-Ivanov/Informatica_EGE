def f(start, end, flag):
    if end > start:
        return 0
    if start == end:
        return flag
    if start == 11:
        flag = 1
    return f(start - 1, end, flag) + f(start - 2, end, flag) + f(start // 3, end, flag)
print(f(16, 6, 0))