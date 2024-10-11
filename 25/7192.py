from fnmatch import fnmatch


def prost(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1


def summ(n):
    return sum([int(i) for i in str(n)])


for i in range(0, 10**9, 2627):
    if fnmatch(str(i), '7*53?3*1') and prost(summ(i)):
        print(i, i // 2627)
