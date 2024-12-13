for x in range(10):
    for y in range(10):
        for z in range(10):
            s = int(f'12{x}345{y}67089{z}')
            if s % 206 == 0:
                print(s, s // 206)