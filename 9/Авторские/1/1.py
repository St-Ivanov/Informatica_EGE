with open('9/Авторские/1/1.txt') as f:
    sp = [[int(i) for i in j.split()] for j in f.readlines()]
k = 0
for i in sp:
    sm = []
    if i.count(max(i)) == 1:
        if len(set(i)) != 6:
            for x in i:
                if i.count(x) > 1:
                    sm.append(x * i.count(x))
            if sum(sm) < max(i):
                k += 1
print(k)