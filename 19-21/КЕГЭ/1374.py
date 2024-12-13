def f(x, y, h):
    if x + y >= 107:
        return h % 2 == 0
    elif h == 0:
        return 0
    else:
        if x * 2 + y > 170 and x + y * 2 > 170:
            ans = [f(x + 10, y, h - 1), f(x, y + 10, h - 1)]
        elif x * 2 + y > 170:
            ans = [f(x + 10, y, h - 1), f(x, y + 10, h - 1), f(x, y * 2, h - 1)]
        elif x + y * 2 > 170:
            ans = [f(x + 10, y, h - 1), f(x, y + 10, h - 1), f(x * 2, y, h - 1)]
        else:
            ans = [f(x + 10, y, h - 1), f(x, y + 10, h - 1), f(x * 2, y, h - 1), f(x, y * 2, h - 1)]
        if h % 2 == 0:
            return any(ans)
        else:
            return any(ans)
print([i for i in range(1, 101) if f(5, i, 2)])
def f(x, y, h):
    if x + y >= 107:
        return h % 2 == 0
    elif h == 0:
        return 0
    else:
        if x * 2 + y > 170 and x + y * 2 > 170:
            ans = [f(x + 10, y, h - 1), f(x, y + 10, h - 1)]
        elif x * 2 + y > 170:
            ans = [f(x + 10, y, h - 1), f(x, y + 10, h - 1), f(x, y * 2, h - 1)]
        elif x + y * 2 > 170:
            ans = [f(x + 10, y, h - 1), f(x, y + 10, h - 1), f(x * 2, y, h - 1)]
        else:
            ans = [f(x + 10, y, h - 1), f(x, y + 10, h - 1), f(x * 2, y, h - 1), f(x, y * 2, h - 1)]
        if h % 2 == 0:
            return all(ans)
        else:
            return any(ans)
print([i for i in range(1, 101) if (f(5, i, 3) and not f(5, i, 1))])
print([i for i in range(1, 101) if (f(5, i, 4) or f(5, i, 2)) and (not f(5, i, 2))])
