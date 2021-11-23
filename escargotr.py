import turtle

turtle.delay(0)
maTortue = turtle.Turtle()
maTortue.speed(0)

for i in range (100000):
    maTortue.left(1*(5000/(i+1)))
    maTortue.forward(1)
input()