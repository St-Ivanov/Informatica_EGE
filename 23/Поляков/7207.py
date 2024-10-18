def f(start, end, flag1, flag2):
    if start > end or start == 15 or start == 30:
        return 0
    if start == end:
        if flag1 and flag2:
            return 1
        else:
            return 0
    if start == 10:
        flag1 = True
    if start == 20:
        flag2 = True
    return f(start + 2, end, flag1, flag2) + f(start + 3, end, flag1, flag2) + f(start ** 2, end, flag1, flag2)
print(f(3, 38, False, False))