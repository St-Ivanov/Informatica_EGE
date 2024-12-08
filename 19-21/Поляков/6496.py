# а
def f(x, y, h):
    if x >= 78 or y >= 78:
        return h % 2 == 0
    elif h == 0:
        return 0
    else:
        ans1 = [f(x + 1, y, h - 1), f(x + 2, y, h - 1), f(x + 3, y, h - 1)]
        ans2 = [f(x, y + 1, h - 1), f(x, y + 2, h - 1), f(x, y + 3, h - 1)]
        if h % 2 == 0:
            if x == y:
                return all(ans1)
            elif x > y:
                return all(ans1 + [f(x, y * 2, h - 1)])
            elif x < y:
                return all(ans2 + [f(x * 2, y, h - 1)])
        else:
            if x == y:
                return any(ans1)
            elif x > y:
                return any(ans1 + [f(x, y * 2, h - 1)])
            elif x < y:
                return any(ans2 + [f(x * 2, y, h - 1)])
print(min([(i + j) for i in range(1, 78) for j in range(1, 78) if f(i, j, 1)]))
print(([i for i in range(1, 78) if (not f(i, 25, 1) and f(i, 25, 3))]))
print(([i for i in range(1, 78) if not f(i, 69, 2) and f(i, 69, 4)]))