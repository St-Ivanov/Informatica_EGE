from turtle import *

speed(1000)
k = 10
left(90)
down()

for i in range(4):
    forward(28 * k)
    right(90)
    forward(26 * k)
    right(90)
up()
forward(8 * k)
right(90)
forward(7 * k)
left(90)
down()
for i in range(4):
    forward(67 * k)
    right(90)
    forward(98 * k)
    right(90)
up()
color('red')
for x in range(0, 27):
    for y in range(0, 29):
        goto(x * k, y * k)
        dot(3)
done()
# 380