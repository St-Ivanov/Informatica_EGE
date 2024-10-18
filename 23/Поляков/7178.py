from functools import lru_cache

@lru_cache(None)
def f(start, end, ch, nch):
    if start % 2 == 0:
        ch += 1
    else:
        nch += 1
    if start > end:
        return 0
    if start == end and ch == nch:
        return 1
    return f(start + 2, end, ch, nch) + f(start + 3, end, ch, nch) + f(start * 3, end, ch, nch)
    
print(sum([int(i) for i in str(f(1, 123, 0, 0))]))
