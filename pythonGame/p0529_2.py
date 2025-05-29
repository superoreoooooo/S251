import turtle
import math

screen = turtle.Screen()
tt = 'pythonGame/imgs/turtle.gif'
screen.addshape(tt)

t = turtle.Turtle()
t.shape(tt)
t.penup()

t.setpos((-300, -200))
t.left(45)

velocity = 75
angle = t.heading()
vx = velocity * math.cos(angle * math.pi / 180.0)
vy = velocity * math.sin(angle * math.pi / 180.0)

print(vy)
x, y = t.pos()

t.pendown()

while True :
    vx = vx
    vy = vy - 10
    
    x = x + vx
    y = y + vy
    
    t.goto(x, y)
    
    if (t.pos()[1] < -200) : break
    
turtle.done()