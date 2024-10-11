B = list(range(70, 91))


for a in range(1, 100):
    k = 0
    for x in range(1, 1001):
        if (x % a == 0) or ((x in B) <= (not (x % 22 == 0))):
            k += 1
    if k == 1000:
        print(a)