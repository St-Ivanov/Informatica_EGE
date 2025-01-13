def f(n):
    n = str(n)
    ret = []
    for i in range(len(n) - 1):
        ret.append(int(n[i] + n[i + 1]))
    return max(ret) - min(ret)
for N in range(10, 10000):
    if f(N) == 44:
        print(N)
        break
