# ((x → y) ∨ (z ≡ x)) ∧ (w → z)
print('x y w z f')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                usl = ((x <= y) or (z == x)) and (w <= z)
                print(x, y, w, z, int(usl))