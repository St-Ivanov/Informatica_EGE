with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\26\КЕГЭ\17687\17687.txt') as f:
    N = f.readline()
    sp = [int(i) for i in f.readlines()]
s = sp
s.sort()
print(sum(s[:len(sp) - len(sp) // 9]))
summa = 0
for i in range(0, len(sp), 9):
    summa += sum(sp[i:i + 9]) - min(sp[i:i + 9])
print(summa)