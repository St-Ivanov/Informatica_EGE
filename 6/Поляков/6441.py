from turtle import *
tracer(0)
screensize(10000, 10000)
k = 10
x = 1
for i in range(7):
    forward(x * k)
    right(90)
    forward(5 * k)
    right(90)
    forward(3 * k)
up()
for x in range(-10, 10):
    for y in range(-10, 10):
        goto(x * k, y * k)
        dot(3, 'red')
done()
for x in range(100000, 0, -1):
    if (x + 2) * (4) < 100000:
        print(x)
        break