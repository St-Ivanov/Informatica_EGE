from turtle import *
tracer(0)
screensize(10000, 10000)
k = 10

for i in range(4):
    forward(3 * k)
    left(270)
    forward(5 * k)
    right(90)
left(270)
for i in range(3):
    forward(5 * k)
    right(90)
    forward(3 * k)
    left(270)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(3, 'red')
done()