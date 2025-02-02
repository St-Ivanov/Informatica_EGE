from math import ceil
for lens in range(1, 1000):
    k = ceil(lens * 9 / 8)
    if (k * 708) / 1024 >= 213:
        print(lens)
        break