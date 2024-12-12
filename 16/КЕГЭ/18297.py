from sys import setrecursionlimit
setrecursionlimit(99999)
def f(n):
    if n < 10:
        return n - 1
    elif n >= 10 and n % 2 == 0:
        return 3 * n - 1 + f(n - 3)
    else:
        return 5 * n + 2 + f(n - 4)
print(f(4445) - f(4444))

a = [0] * 5000
for n in range(len(a)):
    if n < 10:
        a[n] = n - 1
    elif n % 2 == 0:
        a[n] = 3 * n - 1 + a[n - 3]
    else:
        a[n] = 5 * n + 2 + a[n - 4]
print(a[4445] - a[4444])