from sys import setrecursionlimit
setrecursionlimit(10000)
from functools import lru_cache
@lru_cache
def f(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return f(n // 2) + 3
    else:
        return 2 * f(n - 1) + 1
ans = []
for i in range(1, 1001):
    ans.append(f(i))
print(len(set(ans)))