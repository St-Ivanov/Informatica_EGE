with open(r'C:\Users\Stepan_\Documents\Informatica\Informatica_EGE\24\КЕГЭ\12946\12946.txt') as f:
    s = f.readline()
for x in '0123456789':
    for y in '0123456789':
        s = s.replace(f'{x}{y}', f'{x} {y}')
alf = ''.join(sorted(list('qwertyuiopasdfghjklzxcvbnm'.upper())))
for x in alf:
    for y in alf:
        s = s.replace(f'{x}{y}', f'{x} {y}')
s = s.split()
print(len(max(s, key=len)))