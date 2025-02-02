from math import ceil
for i in range(1, 1000):
    if 693 * 1024 * 8 / 2000 >= ceil(i * 11 / 8) * 8:
        print(i)