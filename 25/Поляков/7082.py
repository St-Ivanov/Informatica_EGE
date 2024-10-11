from fnmatch import fnmatch


def delitely(n):
    ret = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ret.append(i)
            if i != n // i:
                ret.append(n // i)
    return list(filter(lambda x: x % 2 == 0, ret))


count = 0
for i in range(65001, 1000000):
    if fnmatch(str(i), '6*97*5?') and len(delitely(i)) >= 4:
        count += 1
        print(i, sum(delitely(i)))
    if count == 7:
        break
