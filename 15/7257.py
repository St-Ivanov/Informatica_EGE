for a in range(1, 1000):
    k = 0
    for x in range(1000):
        if ((x & 156 != 0) or (x & 436 != 0)) <= (x & a > 0):
            k += 1
    if k == 1000:
        print(a)
        break