for A in range(32765, 40000):
    k = 0
    for x in range(40000):
        if ((x & 32765 != 0) or (x & 22635 != 0)) <= (x & A > 0):
            k += 1
    if k == 40000:
        print(A)
        break