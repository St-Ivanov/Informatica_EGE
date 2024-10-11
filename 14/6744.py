def ch(a):
    a = a[::-1]
    return sum(a[i] * 23 ** i for i in range(len(a)))


for i in range(0, 23):
    if (ch([7, i, 3, 8, 5, 9, 6]) + ch([1, 4, i, 3, 6]) + ch([6, 1, i, 7])) % 22 == 0:
        print((ch([7, i, 3, 8, 5, 9, 6]) + ch([1, 4, i, 3, 6]) + ch([6, 1, i, 7])) // 22)
        break