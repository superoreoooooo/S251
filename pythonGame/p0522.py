import turtle

t = turtle.Turtle()
t.shape('turtle')
t.screen.bgcolor('black')
t.speed(0)

"""
def drawRectangle() :
    t.begin_fill()    
    for _ in range(0, 4, 1) :
        t.forward(100)
        t.left(90)
    t.end_fill()
    
colors = ['red', 'blue', 'green', 'yellow']

for c in colors :
    t.color(c)
    t.circle(100)
    # drawRectangle()
    t.left(90)
"""

colors = ['black', "white"]

for i in range(2000) :
    t.pencolor(colors[i % len(colors)])
    t.forward(i)
    t.left(60)

turtle.done()