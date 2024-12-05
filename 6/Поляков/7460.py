from turtle import *
speed(1000)
k = 10
left(90)
down()
tracer(0)


for i in range(9):
    forward(22 * k)
    right(90)
    forward(6 * k)
    right(90)
up()
forward(1 * k)
right(90)
forward(5 * k)
left(90)
down()
for i in range(9):
    forward(53 * k)
    right(90)
    forward(75 * k)
    right(90)
up()

color("red")
for x in range(0, 100):
    for y in range(0, 24):
        goto(x * k, y * k)
        dot(3)

done()
# 44