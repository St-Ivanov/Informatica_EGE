from fnmatch import fnmatch


for i in range(0, 10**9, 13):
    if fnmatch(str(i), '24*68?35'):
        if all([int(x) % 2 == 0 for x in str(i)[2:-5]]) and int(str(i)[-3]) % 3 == 0 and int(str(i)[-3]) % 2 == 1:
            print(i, i // 13)