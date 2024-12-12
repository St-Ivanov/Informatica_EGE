from sys import setrecursionlimit
setrecursionlimit(9999)
def f(n):
    if n == 1:
        return 1
    else:
        return n + f(n - 1)
s = f(2023)
k = 0
for n in range(1, 101):
    if (s // f(n)) % 2 == 0:
        k += 1
print(k)

a = [0] * 2100
k = 0
for n in range(len(a)):
    if n == 1:
        a[n] = 1
    else:
        a[n] = n + a[n - 1]
s = a[2023]
for n in range(1, 100):
    if s // a[n] % 2 == 0:
        k += 1
print(k)