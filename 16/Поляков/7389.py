from sys import setrecursionlimit
setrecursionlimit(10 ** 8)
from functools import lru_cache
@lru_cache
def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return 3 * f(n - 2) + f(n - 1)
print(f(24)//f(20))