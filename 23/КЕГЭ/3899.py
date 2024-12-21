from math import prod
def f(x, y):
    if x == y:
        return 1
    elif x < 10:
        return 0
    return f(prod([int(i) for i in str(x)]), y) + f(sum([int(i) for i in str(x)]), y)
k = 0
for i in range(10, 100):
    if f(i, 8) > 0:
        k += 1
print(k)