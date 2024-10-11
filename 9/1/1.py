with open(r'9/1/4.txt') as f:
    sp = [[int(j) for j in i.split()] for i in f.readlines()]

# k = 0
# for a in sp:
#     povt = 0
#     for x in a:
#         if a.count(x) == 3:
#             povt = x
#             break
#     if len(set(a)) == 4 and (povt * 3) ** 2 > (sum(a) - povt * 3) ** 2:
#         k += 1
# print(k)

k = 0
for i in sp:
    mas_kol = [0] * 6
    summ_povt = 0
    for j in range(6):
        mas_kol[j] = i.count(i[j])
        if mas_kol[j] == 3:
            summ_povt += i[j]
    if mas_kol.count(3) == 3 and mas_kol.count(1) == 3:
        if summ_povt ** 2 > (sum(i) - summ_povt) ** 2:
            k += 1
print(k)