import turtle, random
import time

img1 = 'pythonGame/imgs/front.gif'
img2 = 'pythonGame/imgs/back.gif'

screen = turtle.Screen()

screen.addshape(img1)
screen.addshape(img2)

t1 = turtle.Turtle()

def flip() :
    coin = random.randint(0, 1)
    print(coin)
    if (coin == 0) :
        t1.shape(img1)
        t1.stamp()
    else :
        t1.shape(img2)
        t1.stamp()
        
for i in range(0, 10, 1) :
    flip()
    screen.mainloop()
    time.sleep(5) # 왜안됨 ?

turtle.done()