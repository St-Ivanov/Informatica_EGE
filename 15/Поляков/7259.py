for A in range(7653, 20000):
    k = 0
    for x in range(10000):
        if ((x & 7653 != 0) or (x & 9751 != 0)) <= (x & A > 0):
            k += 1
    if k == 10000:
        print(A)
        break