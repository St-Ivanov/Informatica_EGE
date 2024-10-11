from sys import setrecursionlimit
setrecursionlimit(10000)
def f(n):
    if n < 2:
        return n
    elif n % 2 == 0:
        return f(n / 2) + 1
    else:
        return f(3 * n + 1) + 1
k = 0
for i in range(1, 101):
    if f(i) > 100:
        k += 1
print(k)