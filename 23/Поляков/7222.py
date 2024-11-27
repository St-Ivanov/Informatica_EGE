from functools import lru_cache
import sys
sys.setrecursionlimit(99999)
@lru_cache(None)
def f(x, y, h1, h2):
    if x > y:
        return 0
    if x == y:
        return h1 * h2
    ml = int(str(x)[-1])
    st = int(str(x)[0])
    if x == 95:
        h1 = True
    if x == 103:
        h2 = True
    if st == 1 and ml == 1:
        return f(x + 1, y, h1, h2)
    elif ml == 1:
        return f(x + 1, y, h1, h2) + f(x + st, y, h1, h2)
    elif st == 1 and ml != 0:
        return f(x + 1, y, h1, h2) + f(x + ml, y, h1, h2)
    elif st == 1:
        return f(x + 1, y, h1, h2)
    elif st == ml:
        return f(x + 1, y, h1, h2) + f(x + st, y, h1, h2)
    elif ml != 0:
        return f(x + 1, y, h1, h2) + f(x + st, y, h1, h2) + f(x + ml, y, h1, h2)
    return f(x + 1, y, h1, h2) + f(x + st, y, h1, h2)
print(f(82, 124, False, False))