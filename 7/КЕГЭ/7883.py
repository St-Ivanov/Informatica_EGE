from math import floor
size = 1920 * 1080 * 16 * 100
count = floor(4 * 1024 * 1024 * 1024 * 8 / size)
size *= count
print((4 * 1024 * 1024 * 1024 * 8 - size) / 8 / 1024)