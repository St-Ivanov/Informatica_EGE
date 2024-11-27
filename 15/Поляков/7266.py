for A in range(200):
    k = 0
    for x in range(300):
        for y in range(300):
            if (3 * x + 2 * y > 95) or (4 * x < 3 * y) or (x + 4 * y < A):
                k += 1
    if k != 90000:
        print(A)