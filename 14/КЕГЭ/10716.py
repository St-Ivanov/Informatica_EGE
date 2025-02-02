def f(a):
    a = a[::-1]
    return sum(a[i] * 150 ** i for i in range(len(a)))

for x in range(150):
    nm = f([5, 1, x, 2, 9]) + f([x, 0, 2, 3])
    if nm % 149 == 0:
        print(nm // 149)