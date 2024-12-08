def f(a, p):
    a = a[::-1]
    return sum([a[i] * p ** i for i in range(len(a))])


for p in range(10, 30):
    for x in range(p):
        for y in range(p):
            for w in range(p):
                for z in range(p):
                    num1 = [z, x, y, x, 8]
                    num2 = [x, y, 7, 2, 9]
                    num3 = [w, z, x, 4, 2]
                    if f(num1, p) + f(num2, p) == f(num3, p):
                        print(f([x, y, z, w], p))
                        exit()
