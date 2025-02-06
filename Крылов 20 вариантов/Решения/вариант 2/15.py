for A in range(1000):
    k = 0
    for x in range(1, 1001):
        if ((x % 14 == 0) <= (not (x % 4 == 0))) or (x + A >= 200):
            k += 1
    if k == 1000:
        print(A)
        break