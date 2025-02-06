print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (y <= z) and (w == (x <= y)) and (not x):
                    print(x, y, w, z)