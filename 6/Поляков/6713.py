from turtle import *

tracer(0)
screensize(10000, 10000)
k = 5
for i in range(2):
    forward(13 * k)
    right(90)
    forward(20 * k)
    right(90)
up()
forward(8 * k)
right(90)
back(3 * k)
left(90)
down()
for i in range(2):
    forward(16 * k)
    right(90)
    forward(8 * k)
    right(90)
up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, "red")

done()
