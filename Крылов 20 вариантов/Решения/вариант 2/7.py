for k in range(1000, 0, -1):
    I = 256 * 2560 * 8 * k
    if I / 163840 <= 250:
        print(k)
        break