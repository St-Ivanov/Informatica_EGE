from sys import setrecursionlimit
setrecursionlimit(10000)
def g(n):
    if n < 10:
        return n
    else:
        return g(n - 2) + 1
def f(n):
    return g(n - 1)
kol = 0
for x in range(1, 101):
    res = f(x)
    if int(res ** 0.5) == res ** 0.5 and res != 0:
        kol += 1
print(kol)