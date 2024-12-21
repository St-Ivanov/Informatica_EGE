with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\24\КЕГЭ\13866\1.txt') as f:
    s = f.readline()
for x in '13579':
    for y in '13579':
        for z in '13579':
            s = s.replace(f'{x}{y}{z}', f'{x}{y} {y}{z}')
s = s.split()
s = [len(i) for i in s]
print(max(s))