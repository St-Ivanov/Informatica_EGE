# (X & 123 ≠ 0 ∨ X & 98 ≠ 0) → (X & 75 = 0 → X & А ≠ 0)
for a in range(1, 1000):
    k = 0
    for x in range(1000):
        if (x & 123 != 0 or x & 98 != 0) <= ((x & 75 == 0) <= (x & a != 0)):
            k += 1
    if k == 1000:
        print(a)
        break