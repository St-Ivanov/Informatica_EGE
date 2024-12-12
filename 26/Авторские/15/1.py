# https://education.yandex.ru/ege/task/a1b96fa1-7cf5-4a10-aa78-e933372024a2
with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\26\Авторские\15\1.txt') as f:
    N, K = [int(i) for i in f.readline().split()]
    chairs = []
    players = []
    for i in range(N):
        chairs.append(int(f.readline()))
    for i in range(K):
        players.append(int(f.readline()))
# Создаём id для игрока и стула
for i in range(len(chairs)):
    chairs[i] = [i + 1, chairs[i]]
for i in range(len(players)):
    players[i] = [i + 1, players[i]]
# Сортируем стулья на числовой прямой
chairs.sort(key=lambda x: x[1])
# Список в котором храним количество игроков, которые бегут к стулу
chairs_num = [[] for i in range(len(chairs))]
# Перебираем игроков
rast = 0
id_last = 0
for id_pl, player in players:
    mn_rast = 10 ** 10
    chair_id = 0
    # Перебираем стулья
    for id_ch, chair in chairs:
        # Если растояние меньше, то запоминаем его
        if abs(player - chair) < mn_rast:
            mn_rast = abs(player - chair)
            chair_id = id_ch
        # Если равно, то берём с минимальным id
        elif abs(player - chair) == mn_rast:
            chair_id = min(chair_id, id_ch)
    # Записываем, что игрок бежит к стулу
    chairs_num[chair_id - 1].append([id_pl, mn_rast])
print(K - len([i for i in chairs_num if len(i) > 0]))
ans = []
mn = -100
# Нам нужно проверить, что игрок первым добежал до стула и его расстояние до стула было максимально среди всех
# Пробегаемся по стульям и игрокам, которые к ним бегут
for chair in chairs_num:
    if chair != []:
        # Ищем игрока, который добежит первым, но при этом будет его расстояние будет самым большим среди всех
        mn = max(mn, min([i[1] for i in chair]))
ans = []
# Пробегаемся по стульям и игрокам, которые к ним бегут
for chair in chairs_num:
    # Берём игрока
    for id, rast in chair:
        # Если он добегает до стула первым и его расстояние максимально...
        if rast == mn:
            # то добавляем в списко его id
            ans.append(id)
# Выводим с самым большим id
print(max(ans))