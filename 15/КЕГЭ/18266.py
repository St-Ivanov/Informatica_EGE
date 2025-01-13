for A in range(0, 100):
    k = 0
    for x in range(1, 1000):
        if (x & 57 == 0) or ((x & 23 == 0) <= (not(x & A == 0))):
            k += 1
    if k == 999:
        print(A)
        break