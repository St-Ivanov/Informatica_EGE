from sys import setrecursionlimit
setrecursionlimit(10000)
from functools import lru_cache
@lru_cache(None)
def f(n):
    if n <= 3:
        return n + 3
    if f(n - 1) % 2 == 0:
        return f(n - 2) + n
    else:
        return f(n - 2) + 2 * n
ans = []
for i in range(40, 51):
    ans.append(f(i))
print(sum(ans))