from turtle import *

left(90)
speed(1000)
k = 20
down()

up()
for i in range(10):
    right(120)
    forward(12 * k)
down()
for i in range(7):
    forward(7 * k)
    right(90)
for i in range(5):
    right(60)
    forward(20 * k)
    right(30)
up()

color('red')
for x in range(5, 25):
    for y in range(-15, 10):
        goto(x * k, y * k)
        dot(3)
done()
# 11