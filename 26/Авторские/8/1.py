'''В некотором вузе на некое направление на М бюджетных мест поступает N абитуриентов, которые сдали ЕГЭ по русскому языку, 
профильной математике, физики и/или информатике. В зачет идет 3 экзамена. Если сданы и физика, и информатика, то в зачет идёт 
максимальный балл из двух предметов. В первую очередь зачисляются те, кто подал оригиналы документов. Необходимо определить 
гарантированно проходной балл. В ответе не нужно указывать полупроходные баллы, с которыми можно и не пройти.
Запишите в ответе два числа: проходной балл с учетом наличия оригиналов документов (на момент запроса) и проходной балл без учета 
наличия оригиналов документов (верхняя оценка).
Входные данные представлены в файле 26-108.txt следующим образом.  В первой строке записаны два числа, разделённые пробелом: N – 
количество абитуриентов (1 ≤ N ≤ 10000), M – количество бюджетных мест на направление (1 ≤ М ≤ 10000). В следующих N строках первое число 
– 0 или 1 (отсутствие/наличие оригиналов документов), далее 3 или 4 отметки: баллы по русскому языку, профильной математике, физике и/или 
информатике.
Пример входного файла:
6 2
0 60 80 90 80
1 61 80 90 80
0 62 80 90 80
1 63 80 90
0 64 80 90
1 65 80 90
С учетом наличия оригиналов документов будут зачислены абитуриенты с баллами 235 и 233, так что проходной бал равен 233. Без учета 
наличия оригиналов документов зачисляются абитуриенты, набравшие 235 и 234 баллов, в этом случае проходной балл 234.'''

with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\26\Авторские\8\1.txt') as f:
    N, M = [int(j) for j in f.readline().split()]
    sp = [i.split() for i in f.readlines()]


orig = []
neorig = []

for m in sp:
    if len(m) == 4:
        if m[0] == '1':
            orig.append(sum([int(i) for i in m[1:]]))
        else:
            neorig.append(sum([int(i) for i in m[1:]]))
    else:
        if m[0] == '1':
            orig.append(sum([int(i) for i in m[1:3]] + [int(max(m[3:]))]))
        else:
            neorig.append(sum([int(i) for i in m[1:3]] + [int(max(m[3:]))]))

orig.sort(reverse=True)
neorig.sort(reverse=True)
neuchet = orig + neorig
neuchet.sort(reverse=True)
print(orig[M - 1], neuchet[M - 1])