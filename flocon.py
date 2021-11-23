from turtle import *
 
def koch(longueur, n):
 
    if n == 0:
        forward(longueur)
    else:
        koch(longueur/3, n-1)
        left(60)
        koch(longueur/3, n-1)
        right(120)
        koch(longueur/3, n-1)
        left(60)
        koch(longueur/3, n-1)
 
def flocon(taille, etape):
    koch(taille, etape)
    right(120)
    koch(taille, etape)
    right(120)
    koch(taille, etape)
 
 
up()
goto(-280, 100)
down()
speed(0)
color("black")
 
flocon(500, 10)
 
input()