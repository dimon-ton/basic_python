import sys

print(sys.version)

import turtle
tao = turtle.Pen()
tao.shape('turtle')

def Rectangle(x):
    for i in range(4):
        tao.fd(x)
        tao.lt(90)

    
def Go(x, y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

Go(100,100)
Rectangle(300)
