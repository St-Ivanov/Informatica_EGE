for A in range(100, 0, -1):
    k = 0
    for x in range(1, 101):
        for y in range(1, 101):
            for z in range(1, 101):
                if (x | 50 == x) or (y & 34 != 0) or (z | 24 != 24) or (x * y * z > A // 8):
                    k += 1
    if k == 1000000:
        print(A)
        break