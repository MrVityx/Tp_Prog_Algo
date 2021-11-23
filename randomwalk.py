import turtle
import random

turtle.delay(0)
turtle.colormode(255)

def colorTurtle (Tortue):
    R = random.randint(0,255)
    G = random.randint(0,255)
    B = random.randint(0,255)
    Tortue.pencolor(R,G,B)

maTortue = turtle.Turtle()
maTortue.speed(0)
colorTurtle(maTortue)

TortueAD1 = turtle.Turtle()
TortueAD1.speed(0)
colorTurtle(TortueAD1)

TortueAD2 = turtle.Turtle()
TortueAD2.speed(0)
colorTurtle(TortueAD2)

TortueAD3 = turtle.Turtle()
TortueAD3.speed(0)
colorTurtle(TortueAD3)


def move (Tortue):
    drift =random.randint(0,2)
    if drift == 0:
        Tortue.left(90)
    elif drift == 2:
        Tortue.right(90)
    Tortue.forward(3)

while 1 != 2:
    move(maTortue)
    move(TortueAD1)
    move(TortueAD2)
    move(TortueAD3)
input()