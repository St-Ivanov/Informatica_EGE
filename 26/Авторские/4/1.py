'''В отделении банка работают шесть окон для обслуживания клиентов. Каждое окно оказывает услуги определённого вида. Клиент входит в 
отделение и встаёт в очередь к тому окну, которое оказывает необходимую ему услугу.
Если после 30 минут ожидания в очереди окно не освободилось, клиент уходит. Если окно освободилось ровно через 30 минут ожидания, 
клиент не уходит и получает услугу.
Если момент завершения обслуживания одного или нескольких клиентов совпадает с моментом прихода нового клиента, то можно считать, что 
новый клиент пришёл после того, как обслуживание ранее пришедшего клиента завершилось и очередь сократилась.
Входные данные.
Первая строка входного файла содержит целое число N (N ≤ 1000)  — общее количество клиентов, пришедших в отделение за один рабочий 
день. Каждая из следующих N строк описывает одного клиента и содержит 3 целых числа: время прихода клиента в отделение (количество 
минут с начала рабочего дня), время (количество минут), необходимое для обслуживания данного клиента, и номер окна, в которое ему 
необходимо обратиться. Гарантируется, что никакие два клиента не приходят в одно и то же время.
Определите наименьшее количество клиентов, обслуженных в течение дня в одном окне, и количество клиентов, которые покинут отделение 
из-⁠за слишком долгого ожидания.
В ответе запишите два целых числа: сначала наименьшее количество клиентов, обслуженных в одном окне, затем количество необслуженных 
клиентов.'''

with open(r'26\Авторские\4\4.txt') as f:
    N = int(f.readline())
    sp = [[int(j) for j in i.split()] for i in f.readlines()]

# Сортируем по времени прихода клиента
sp.sort(key=lambda x: x[0])
# Создаём очереди для каждого окна
okna = [[0] for i in range(7)]
# Счётчик для тех, кто свалил домой
yshel = 0
for start, cont, window in sp:
    # если клиент придёт раньше
    if start <= okna[window][-1]:
        # если очередь окажется больше 30
        if okna[window][-1] - start > 30:
            yshel += 1
            continue
        else:
            okna[window].append(okna[window][-1] + cont)
    # если пришёл позже
    else:
        okna[window].append(start + cont)
# выводим минимальное по длине обслуженных клиентов и не берём 0 окно, так как его нет
print(min([len(i) for i in okna[1:]]) - 1, yshel)