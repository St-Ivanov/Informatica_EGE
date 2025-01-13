B = range(70, 91)
for A in range(1000, 0, -1):
    k = 0
    for x in range(1, 1000):
        if (x % A == 0) or ((x in B) <= (not(x % 22 == 0))):
            k += 1
    if k == 999:
        print(A)
        break