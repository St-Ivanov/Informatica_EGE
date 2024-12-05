from turtle import *
tracer(0)
screensize(10000, 10000)
k = 10
for i in range(3):
    left(90)
    for m in range(4):
        forward(5 * k)
        right(90)
up()
for x in range(-10, 10):
    for y in range(-10, 10):    
        goto(x * k, y * k)
        dot(3, "red")
done()