for A in range(100):
    k = 0
    for x in range(1, 301):
        if (((x % 9 == 0) <= (not(x % 6 == 0))) or (x + A >= 100)):
            k += 1
    if k == 300:
        print(A)
        break