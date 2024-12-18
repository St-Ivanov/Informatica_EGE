''' Главному инженеру фабрики дали задачу написать программу для раскладки N деталей в K контейнеров, каждый из которых рассчитан на 
свой определённый объём. Все детали кладут по очереди. Каждую следующую деталь стараются положить в контейнер с наименьшим 
возможным номером. Укажите в ответе два числа: объём всех отложенных деталей и их количество.
Формат входных данных.
В первых двух строках входного файла записаны значения N (количество деталей), K (количество контейнеров). Следующие N строк содержат по 
одному целому числу  — объём очередной детали. Следующие K строк содержат по одному целому числу  — объём каждого контейнера.
Формат выходных данных.
Программа должны вывести два числа: первое число равно объёму всех отложенных деталей, второе число  — их количество.
Входные данные.
В первой строке входного файла находится число N  — количество деталей (натуральное число, не превышающее 20 000). Во второй строке 
число K  — количество конвейеров (натуральное число, не превышающее 20 000). Первые N строк содержат одно целое число  — объём 
очередной детали. Следующие K строк содержат объём каждого конвейера.
Выходные данные.
Два целых неотрицательных числа: первое число равно объёму всех отложенных деталей, второе число  — их количество.'''
sp_det = []
sp_kon = []
with open(r'26\Авторские\3\3.txt') as f:
    N = int(f.readline())
    K = int(f.readline())
    for i in range(N):
        sp_det.append(int(f.readline()))
    for i in range(K):
        sp_kon.append(int(f.readline()))


ans = []
for detal in sp_det:
    for konteiner in range(len(sp_kon)):
        if sp_kon[konteiner] >= 0:
            sp_kon[konteiner] -= detal
            ans.append(detal)
            break
print(sum(ans), len(ans))
