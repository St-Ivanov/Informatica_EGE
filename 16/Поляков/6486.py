from sys import setrecursionlimit
from functools import lru_cache
setrecursionlimit(10000)
@lru_cache(None)
def f(n):
    if n > 2000000:
        return n
    else:
        return 7 * n + f(3 * n)
def g(n):
    return f(n) / n
s = g(12345)
kol = 0
for i in range(1, 100000):
    if g(i) == s:
        kol += 1
print(kol)