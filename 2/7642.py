# ((w → y) → x) ˅ ¬z
print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (((x <= y) <= x) or not(z)) == False:
                    print(x, y, w, z)