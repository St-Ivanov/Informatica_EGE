from sys import setrecursionlimit
from functools import lru_cache
setrecursionlimit(9999)
@lru_cache(None)
def f(n):
    if n < 3:
        return 2
    elif n % 2 == 0:
        return 2 * f(n - 2) - f(n - 1) + 2
    else:
        return 2 * f(n - 1) + f(n - 2) - 2
print(f(170))


a = [0] * 200
for n in range(len(a)):
    if n < 3:
        a[n] = 2
    elif n % 2 == 0:
        a[n] = 2 * a[n - 2] - a[n - 1] + 2
    else:
        a[n] = 2 * a[n - 1] + a[n - 2] - 2
print(a[170])