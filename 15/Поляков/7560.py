for A in range(0, 100):
    k = 0
    for x in range(0, 300):
        for y in range(0, 300):
            if (x + y <= 30) or (y <= x + 2) or (y >= A):
                k += 1
    if k == 90000:
        print(A)