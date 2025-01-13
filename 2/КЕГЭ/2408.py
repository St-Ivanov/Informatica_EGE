print('c a b f')
for c in range(2):
    for a in range(2):
        for b in range(2):
            f = (not a) or (b and (not c))
            print(a, b, c, int(f))