import turtle
import random

turtle.delay(0)
turtle.colormode(255)

tortues = []

def colorTurtle (Tortue):
    R = random.randint(0,255)
    G = random.randint(0,255)
    B = random.randint(0,255)
    Tortue.color(R,G,B)

def startpos (Tortue):
    X = random.randint(-250,250)
    Y = random.randint(-250,250)
    Tortue.setposition(X, Y)

def coliTortue (Tortue1, Tortue2):
    distance = (Tortue1.xcor()-Tortue2.xcor())**2 + (Tortue2.ycor()-Tortue1.ycor())**2
    distance**(0.5)
    if distance < (Tortue1.shapesize()[0]+Tortue2.shapesize()[0])*100 :
        if Tortue1.shapesize() < Tortue2.shapesize():
            Tortue2.shapesize(Tortue2.shapesize()[0]+Tortue1.shapesize()[0],Tortue2.shapesize()[1]+Tortue1.shapesize()[1])
            Tortue1.hideturtle()
            return (tortues.remove(Tortue1))
        elif Tortue1.shapesize() > Tortue2.shapesize():
            Tortue1.shapesize(Tortue2.shapesize()[0]+Tortue1.shapesize()[0],Tortue2.shapesize()[1]+Tortue1.shapesize()[1])
            Tortue2.hideturtle()
            return (tortues.remove(Tortue2))
        else:
            choix = random.randint(0,1)
            if choix == 1:
                Tortue1.shapesize(Tortue2.shapesize()[0]+Tortue1.shapesize()[0],Tortue2.shapesize()[1]+Tortue1.shapesize()[1])
                Tortue2.hideturtle()
                return (tortues.remove(Tortue2))
            else:
                Tortue2.shapesize(Tortue2.shapesize()[0]+Tortue1.shapesize()[0],Tortue2.shapesize()[1]+Tortue1.shapesize()[1])
                Tortue1.hideturtle()
                return (tortues.remove(Tortue1))

for i in range (10):
    tortues.append(turtle.Turtle())
    tortues[i].speed(1)
    tortues[i].penup()
    colorTurtle(tortues[i])
    startpos(tortues[i])
    tortues[i].shapesize(1)
    tortues[i].shape("circle")

def move (Tortue):
    drift =random.randint(0,2)
    if drift == 0:
        Tortue.left(90)
    elif drift == 2:
        Tortue.right(90)
    Tortue.forward(5)

MyTortue = turtle.Turtle()
MyTortue.speed(1)
MyTortue.penup()
MyTortue.shapesize(1)
MyTortue.shape("circle")

def tleft():
    MyTortue.left(90)

def tright():
    MyTortue.right(90)

turtle.listen()
turtle.onkeypress(tleft,"q")
turtle.onkeypress(tright,"d")


while 1 != 2:
    MyTortue.forward(5)

    for i in tortues:
        move(i)

    for i in tortues:
        coliTortue(MyTortue,i)
        for y in tortues:
            if i != y:
                coliTortue(i, y)
input()