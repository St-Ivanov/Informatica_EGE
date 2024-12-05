# а
def f(x, h):
    if x >= 61:
        return h == 0
    elif h == 0:
        return 0
    else:
        # проверяем случай, если за ход получаем больше 80 камней и он нам не подходит, такого не может быть
        if x * 2 > 80:
            if h % 2 == 0:
                return f(x + 1, h - 1)
            else:
                return f(x + 1, h - 1)
        else:
            if h % 2 == 0:
                return all([f(x + 1, h - 1), f(x * 2, h - 1)])
            else:
                return any([f(x + 1, h - 1), f(x * 2, h - 1)])
print(len([i for i in range(1, 61) if f(i, 1)]))

# # б
def f(x, h):
    if x >= 61:
        return h == 0
    elif h == 0:
        return 0
    else:
        # проверяем случай, если за ход получаем больше 80 камней и он нам не подходит, такого не может быть
        if x * 2 > 80:
            if h % 2 == 0:
                return f(x + 1, h - 1)
            else:
                return f(x + 1, h - 1)
        else:
            if h % 2 == 0:
                return all([f(x + 1, h - 1), f(x * 2, h - 1)])
            else:
                return any([f(x + 1, h - 1), f(x * 2, h - 1)])
print(([i for i in range(1, 61) if f(i, 3) and not f(i, 1)])[:2])

# б
def f(x, h):
    if x >= 61:
        return h == 0
    elif h == 0:
        return 0
    else:
        # проверяем случай, если за ход получаем больше 80 камней и он нам не подходит, такого не может быть
        if x * 2 > 80:
            if h % 2 == 0:
                return f(x + 1, h - 1)
            else:
                return f(x + 1, h - 1)
        else:
            if h % 2 == 0:
                return all([f(x + 1, h - 1), f(x * 2, h - 1)])
            else:
                return any([f(x + 1, h - 1), f(x * 2, h - 1)])
print(([i for i in range(1, 61) if (f(i, 4) or f(i, 2)) and not f(i, 2)]))