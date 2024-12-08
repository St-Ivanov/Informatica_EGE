def f(n, k):
    s = ''
    while n != 0:
        s += str(n % k)
        n //= k
    return s[::-1]


def prost(n):
    ret = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            ret.append(i)
            if n // i != i:
                ret.append(n // i)
    return len(ret) == 0


def sm(n):
    return sum([int(i) for i in str(n)])


ans = []
for i in range(2, 11):
    s = f(437, i)
    if prost(sm(int(s))):
        ans.append(i)
print(sum(ans))