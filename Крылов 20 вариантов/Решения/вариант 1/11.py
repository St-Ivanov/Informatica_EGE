from math import ceil
for lens in range(1000, 1, -1):
    I = ceil(11 * lens / 8) # байт
    if 3000 * I <= 555 * 1024:
        print(lens)
        break