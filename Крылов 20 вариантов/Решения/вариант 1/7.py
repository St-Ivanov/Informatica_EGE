for kol in range(100, 0, -1):
    if (kol * 8 * 768 * 5120) / 655360 <= 500:
        print(kol)
        break
print(655360 * 500 / 8 / 768 / 5120)