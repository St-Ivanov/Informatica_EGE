def f(start, end, flag1, flag2):
    if start == 8:
        flag1 = 1
    if start == 23:
        flag2 = 1
    if start < end:
        return 0
    if start == end:
        if flag1 and flag2:
            return 0
        else:
            return 1
    return f(start - 4, end, flag1, flag2) + f(start // 2, end, flag1, flag2)
print(f(39, 4, 0, 0))