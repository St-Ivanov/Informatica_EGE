def f(start, end, flag):
    if start > end:
        return 0
    if start == end:
        return flag
    if start == 7:
        flag = 1
    return f(start + 1, end, flag) + f(start + 2, end, flag) + f(start + 3, end, flag)
print(f(5, 11, 0))