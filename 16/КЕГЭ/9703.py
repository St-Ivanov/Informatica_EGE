a = [0] * 100
for n in range(len(a)):
    if n < 2:
        a[n] = n
    else:
        a[n] = a[n // 2] + a[n % 2]
for n in range(len(a)):
    print(bin(n)[2:], a[n])
print((bin(2 ** 30)[2:]))
from math import factorial
print(factorial(30) / (factorial(27) * factorial(3))) # C из n по k 