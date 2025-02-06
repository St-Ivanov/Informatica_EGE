from math import ceil
for lens in range(1000, 0, -1):
    I = ceil(lens * 10 / 8) # байт
    if 1500 * I <= 780 * 1024:
        print(lens)
        break