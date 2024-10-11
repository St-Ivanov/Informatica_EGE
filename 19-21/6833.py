def f(s, h):
    if s >= 37 and (h == 5 or h == 3):
        return True
    elif h == 5 and s < 37:
        return False
    elif h < 5 and s >= 37:
        return False
    else:
        if h % 2 != 0:
            return f(s + 1, h + 1) and f(s + 2, h + 1) and f(s * 3, h + 1) # ход Пети
        else:
            return f(s + 1, h + 1) or f(s + 2, h + 1) or f(s * 3, h + 1) # ход Вани

def f1(s, h):
    if s >= 37 and h == 3:
        return True
    elif h == 3 and s < 37:
        return False
    elif h < 3 and s >= 37:
        return False
    else:
        if h % 2 != 0:
            return f1(s + 1, h + 1) and f1(s + 2, h + 1) and f1(s * 3, h + 1) # ход Пети
        else:
            return f1(s + 1, h + 1) or f1(s + 2, h + 1) or f1(s * 3, h + 1) # ход Вани

for x in range(1, 37):
    if f(x, 1):
        print('1', x)
    if f1(x, 1):
        print('2', x)
