for a in range(1000, 0, -1):
    k = 0
    for x in range(0, 300):
        for y in range(0, 300):
            if (3 * x + 2 * y > 25) or (x > 2 * y) or (x + 4 * y < a):
                k += 1
    if k != 90000:
        print(a)
        break
