"""
№2. В отделении банка работают два окна для обслуживания клиентов. Некоторые 
услуги могут быть оказаны только при обращении в определённое окно, 
некоторые  — при обращении в любое окно. Клиент входит в отделение и встаёт 
в очередь к тому окну, которое оказывает необходимую ему услугу. Если услуга 
может быть оказана в любом окне, клиент выбирает то, в очереди к которому в 
данный момент меньше людей. Если очереди в оба окна одинаковые, клиент 
выбирает окно с меньшим номером. При этом если в очереди к выбранному окну 
уже стоит 12 или более человек (включая человека, которого обслуживают в 
данный момент), пришедший клиент сразу уходит.
Если момент завершения обслуживания одного или нескольких клиентов 
совпадает с моментом прихода нового клиента, то можно считать, что новый 
клиент пришёл после того, как обслуживание ранее пришедшего клиента 
завершилось и очередь сократилась.
Входные данные.
Первая строка входного файла содержит целое число N (N ≤ 1000)  — общее 
количество клиентов, пришедших в отделение за один рабочий день. Каждая из 
следующих N строк описывает одного клиента и содержит 3 целых числа: время 
прихода клиента в отделение (количество минут с начала рабочего дня), время, 
необходимое для обслуживания данного клиента, и номер окна, в которое ему 
необходимо обратиться (0 означает, что клиент может обратиться в любое окно). 
Гарантируется, что никакие два клиента не приходят одновременно.
Определите, сколько клиентов будет обслужено в течение дня в окне номер 1 и 
сколько клиентов покинет отделение из-⁠за слишком больших очередей.
В ответе запишите два целых числа: сначала количество клиентов, обслуженных в 
окне номер 1, затем количество необслуженных клиентов.
Ответ: 118 467.
"""
with open('2.txt') as f:
    N = int(f.readline())
    sp = [[int(j) for j in i.split()] for i in f.readlines()]


sp.sort(key=lambda x: x[0])

ushel = []
kol = 0

window1 = [False] * 12
window2 = [False] * 12
for start, cont, wind in sp:
    print(start, cont, wind, window1, window2)
    if wind == 1:
        for m in window1:
            if m == False:
                break
            if m <= start:
                window1.pop(0)
                window1.append(False)
                kol += 1
        if window1.count(False) == 0:
            ushel.append(start)
            continue
        else:
            if window1.count(False) == 12:
                window1[window1.index(False)] = start + cont
            else:
                window1[window1.index(False)] = window1[window1.index(False)-1] + cont
    if wind == 2:
        for m in window2:
            if m == False:
                break
            if m <= start:
                window2.pop(0)
                window2.append(False)
        if window2.count(False) == 0:
            ushel.append(start)
            continue
        else:
            if window2.count(False) == 12:
                window2[window2.index(False)] = start + cont
            else:
                window2[window2.index(False)] = window2[window2.index(False)-1] + cont
    if wind == 0:
        if window1.count(False) >= window2.count(False):
            for m in window1:
                if m == False:
                    break
                if m <= start:
                    window1.pop(0)
                    window1.append(False)
                    kol += 1
            if window1.count(False) == 0:
                ushel.append(start)
                continue
            else:
                if window1.count(False) == 12:
                    window1[window1.index(False)] = start + cont
                else:
                    window1[window1.index(False)] = window1[window1.index(False)-1] + cont
        else:
            for m in window2:
                if m == False:
                    break
                if m <= start:
                    window2.pop(0)
                    window2.append(False)
            if window2.count(False) == 0:
                ushel.append(start)
                continue
            else:
                if window2.count(False) == 12:
                    window2[window2.index(False)] = start + cont
                else:
                    window2[window2.index(False)] = window2[window2.index(False)-1] + cont
print(kol + 12 - window1.count(False), ushel)


    
        
