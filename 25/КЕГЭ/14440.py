from math import prod
def delitely(n):
    ret = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            ret.append(i)
            if n // i != i:
                ret.append(n // i)
    return list(set(ret))
ans = []
for x in range(10):
    for y in range(10):
        s = int(f'31{x}567{y}')
        if len(delitely(s)) == 0:
            ans.append(s)
for x in range(10):
    s = int(f'31567{x}')
    if len(delitely(s)) == 0:
        ans.append(s)
ans.sort()
for i in ans:
    print(i, prod([int(j) for j in str(i)]))
