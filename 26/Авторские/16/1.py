# https://education.yandex.ru/ege/task/ae9c3bc9-15d5-4084-afc7-e24d3f646570
with open(r'C:\Users\si655\OneDrive\Документы\Informatica_EGE\26\Авторские\16\1.txt') as f:
    N = int(f.readline())
    sp = [int(i) for i in f.readlines()]
sp.sort()
sp_clikov_5 = []
# Перебираем клики
kol = 0
k = 0
mx = 0
for click in sp:
    l = []
    for i in sp_clikov_5:
        if i + 1000 > click:
            l.append(i)
        else:
            break
    sp_clikov_5 = l
    if len(sp_clikov_5) != 5:
        kol += 1
        sp_clikov_5.append(click)
        mx = max(mx, k)
        k = 0
    else:
        k += 1
print(kol, mx)
