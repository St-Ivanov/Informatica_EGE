from sys import setrecursionlimit
setrecursionlimit(10000)
def f(n):
    if n < 7:
        return 7
    if n % 3 != 0:
        return 5 - f(n - 1)
    else:
        return 3 + f(n - 1)
print(f(3015))