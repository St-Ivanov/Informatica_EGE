def delitely(n):
    ret = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ret.append(i)
            if n // i != i:
                ret.append(n // i)
    return sum(ret)

def f(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    return f(start + 1, end) + f(start + delitely(start), end)
print(f(2, 62))