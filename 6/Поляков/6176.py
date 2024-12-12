from turtle import *
tracer(0)
screensize(10000, 10000)
k = 10
for i in range(2):
    forward(20 * k)
    right(90)
    forward(25 * k)
    right(90)
right(90)
forward(13 * k)
right(90)
forward(7 * k)
for i in range(4):
    left(90)
    forward(7 * k)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, 'red')
done()
# от 7 до 27