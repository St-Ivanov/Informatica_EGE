for a in range(100000):
    k = 0
    for x in range(1, 10001):
        if (x & 2735 != 0) <= ((x & 1234 == 0) <= (x & a != 0)):
            k += 1
    if k == 10000:
        print(a)
        break