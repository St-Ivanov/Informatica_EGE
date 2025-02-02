for A in range(0, 100):
    k = 0
    for x in range(15, 31):
        if (x & 29 == 0) or ((x & 11 == 0) <= (not (x & A == 0))):
            k += 1
    if k == 16:
        print(A)
        break