for a in range(100, 1, -1):
    k = 0
    for x in range(300):
        for y in range(300):
            if (x + 2 * y > a) or (y < x) or (x < 30):
                k += 1
    if k == 90000:
        print(a)
        break
