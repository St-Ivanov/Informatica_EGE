def f(x, y, z, h):
    if x + y + z >= 73:
        return h % 2 == 0
    elif h == 0:
        return 0
    else:
        ans1 = [f(x + i, y, z, h - 1) for i in [3, 13, 23]]
        ans2 = [f(x, y + i, z, h - 1) for i in [3, 13, 23]]
        ans3 = [f(x, y, z + i, h - 1) for i in [3, 13, 23]]
        if h % 2 == 0:
            return any(ans1 + ans2 + ans3)
        else:
            return any(ans1 + ans2 + ans3)
print([i for i in range(1, 24) if f(2, i, 2 * i, 2)])
def f1(x, y, z, h):
    if x + y + z >= 73:
        return h % 2 == 0
    elif h == 0:
        return 0
    else:
        ans1 = [f1(x + i, y, z, h - 1) for i in [3, 13, 23]]
        ans2 = [f1(x, y + i, z, h - 1) for i in [3, 13, 23]]
        ans3 = [f1(x, y, z + i, h - 1) for i in [3, 13, 23]]
        if h % 2 == 0:
            return all(ans1 + ans2 + ans3)
        else:
            return any(ans1 + ans2 + ans3)
print([i for i in range(1, 24) if f1(2, i, 2 * i, 3) and not f1(2, i, i * 2, 1)])
def f(x, y, z, h):
    if x + y + z >= 73:
        return h == 0
    elif h == 0:
        return 0
    else:
        ans1 = [f(x + i, y, z, h - 1) for i in [3, 13, 23]]
        ans2 = [f(x, y + i, z, h - 1) for i in [3, 13, 23]]
        ans3 = [f(x, y, z + i, h - 1) for i in [3, 13, 23]]
        if h % 2 == 0:
            return all(ans1 + ans2 + ans3)
        else:
            return any(ans1 + ans2 + ans3)
print([i for i in range(1, 24) if (f1(2, i, i * 2, 4) or f1(2, i, i * 2, 2)) and not (f(2, i, i * 2, 4) or f(2, i, i * 2, 2))])