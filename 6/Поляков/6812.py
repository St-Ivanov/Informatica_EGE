from turtle import *

left(90)
speed(1000)
k = 20
down()

right(90)
for i in range(3):
    right(45)
    forward(10 * k)
    right(45)
right(315)
forward(10 * k)
for i in range(2):
    right(90)
    forward(10 * k)

up()
color('red')
for x in range(-15, 50):
    for y in range(-20, 10):
        goto(x * k, y * k)
        dot(3)
done()
# 203