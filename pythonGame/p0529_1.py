import turtle

screen = turtle.Screen()
img1 = 'pythonGame/imgs/rabbit.gif'
img2 = 'pythonGame/imgs/turtle.gif'

screen.addshape(img1)
screen.addshape(img2)

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.shape(img1)
t1.penup()
t1.goto(-300, 0)

t2.shape(img2)
t2.penup()
t2.goto(-300, -200)

t1.pendown()
t2.pendown()

import random

for i in range(10) :
    d1 = random.randint(1, 60)
    d2 = random.randint(1, 60)
    t1.forward(d1)
    t2.forward(d2)

turtle.done()