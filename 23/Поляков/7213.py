from functools import lru_cache

@lru_cache(None)
def f(start, end, h, flag):
    if start > end + 5 or abs(start) % 10 == 3:
        return 0
    if start == 60:
        flag = 1
    if start == end:
        return flag
    if h == 0:
        return f(start - 1, end, 1, flag) + f(start - 5, end, 1, flag) + f(start + 7, end, 0, flag) + f(start * 2, end, 0, flag)
    else:
        return f(start + 7, end, 0, flag) + f(start * 2, end, 0, flag)
print(f(9, 84, 0, 0))