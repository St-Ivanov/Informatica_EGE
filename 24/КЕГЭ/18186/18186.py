with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\24\КЕГЭ\18186\1.txt') as f:
    s = f.readline()
for x in 'BCDFGH':
    for y in 'BCDFGH':
        for z in 'AE':
            s = s.replace(f'{x}{y}{z}', ' ')
s = s.split()
s = [len(i) for i in s]
print(max(s) + 6)