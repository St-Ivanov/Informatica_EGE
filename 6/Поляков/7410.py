from turtle import *

tracer(0)
screensize(10000, 10000)
k = 5
down()
right(90)
for i in range(10):
    right(45)
    forward(203 * k)
    right(45)
up()
back(40 * k)
right(45)
down()
for i in range(5):
    forward(20 * k)
    left(90)
up()

for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(3, "red")
input()
# ?