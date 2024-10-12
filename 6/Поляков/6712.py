from turtle import *

speed(1000)
k = 20
left(90)
down()

for i in range(2):
    forward(10 * k)
    right(90)
    forward(18 * k)
    right(90)
up()
forward(5 * k)
right(90)
forward(7 * k)
left(90)
down()
for i in range(2):
    forward(10 * k)
    right(90)
    forward(7 * k)
    right(90)
up()

color('red')
for x in range(0, 19):
    for y in range(0, 20):
        goto(x * k, y * k)
        dot(3)
done()
# 249