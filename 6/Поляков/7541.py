from turtle import *

down()
speed(10000)
left(90)
k = 10

for i in range(10):
    forward(22 * k)
    right(90)
    forward(16 * k)
    right(90)
up()
forward(1 * k)
right(90)
forward(1 * k)
left(90)
down()
for i in range(10):
    forward(72 * k)
    right(90)
    forward(79 * k)
    right(90)
up()

for x in range(0, 100):
    for y in range(0, 30):
        goto(x * k, y * k)
        color("red")
        dot(3)
done()
# 72
