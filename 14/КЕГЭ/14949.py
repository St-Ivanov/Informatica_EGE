sp = [2 ** i for i in range(30)]
s = '01234567'
for x in s:
    nm = int(f'{x}1{x}', 16) + int(f'{x}3{x}3', 8)
    if nm in sp:
        print(x)