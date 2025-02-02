for A in range(999, 1, -1):
    k = 0
    for x in range(1, 200001):
        if (((x % A == 0) and (x % 37 == 0)) <= (x % 3737 == 0)) and (A < 1000):
            k += 1
    if k == 200000:
        print(A)
        break