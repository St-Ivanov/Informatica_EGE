from turtle import *

tracer(0)
screensize(10000, 10000)
k = 5

for i in range(2):
    forward(5 * k)
    right(90)
    forward(11 * k)
    right(90)
up()
back(4 * k)
right(90)
forward(6 * k)
left(90)
down()
for i in range(2):
    forward(42 * k)
    right(90)
    forward(63 * k)
    right(90)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(3, "red")
done()