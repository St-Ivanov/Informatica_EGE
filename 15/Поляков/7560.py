for a in range(1, 100):
    k = 0
    for x in range(1, 101):
        for y in range(1, 101):
            if (x + y <= 30) or (y <= x + 2) or (y >= a):
                k += 1
    if k == 10000:
        print(a)