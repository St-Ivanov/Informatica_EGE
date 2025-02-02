for A in range(300, 1, -1):
    k = 0
    for x in range(1, 301):
        if ((not (x % 7 == 0)) and (x % 13 == 0)) <= (x > A - 40):
            k += 1
    if k == 300:
        print(A)
        break