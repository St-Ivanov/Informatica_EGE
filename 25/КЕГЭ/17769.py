from fnmatch import fnmatch
for i in range(0, 10 ** 10, 2025):
    if fnmatch(str(i), '21?3*145?5'):
        print(i, i // 2025)