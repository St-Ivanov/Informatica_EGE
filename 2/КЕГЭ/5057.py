print('x y w z f')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                ans = (w <= (y == z)) and (y == (z <= x))
                print(x, y, w, z, int(ans))