from itertools import permutations
k = 0
no = [j + i for j in '1357' for i in '1357'] + [j + i for j in '02468' for i in '02468']
for i in permutations('012345678', r=7):
    if i[0] != '0' and i.count('2') == 0:
        f = True
        s = ''.join(i)
        for m in no:
            if m in s:
                f = False
                break
        if f:
            k += 1
print(k)