def f(x,y, n):
    if x + y >= 62: return n == 0
    if n == 0: return False
    ans = [f(x+y, y, n-1), f(x, x +y, n-1)]
    if n % 2 != 0:
        return any(ans)
    else:
        return all(ans)
print([i for i in range(1,52) if f(10, i, 1)][0])
print([i for i in range(1,52) if f(10, i, 3) and not f(10, i, 1)])
print(len([i for i in range(1,52) if (f(10, i, 4) or f(10, i, 2)) and not f(10, i, 2)]))
