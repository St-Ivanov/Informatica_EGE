def f(start, end, flag):
    if start == 14:
        flag = 1
    if start == end:
        return flag
    if end > start:
        return 0
    else:
        return f(start - 2, end, flag) + f(start // 2, end, flag)
print(f(32, 1, 0))