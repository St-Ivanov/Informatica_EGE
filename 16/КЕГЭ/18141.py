from sys import setrecursionlimit
setrecursionlimit(99999)
def f(n):
    if n <= 10:
        return n
    elif n % 2 == 0:
        return 2 * f(n - 2) + 6
    else:
        return f(n - 1) + 2 * n
print(sum([int(i) for i in str(f(27) - f(20))]))

a = [0] * 100
for n in range(len(a)):
    if n <= 10:
        a[n] = n
    elif n % 2 == 0:
        a[n] = 2 * a[n - 2] + 6
    else:
        a[n] = a[n - 1] + 2 * n
print(sum([int(i) for i in str(a[27] - a[20])]))