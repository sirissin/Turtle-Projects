from turtle import *
from random import *

#Screen properties
title("Starry Night")
bgcolor('black')
hideturtle()


#Draw a Star
def draw_star(xpos, ypos):
    size = randrange(4, 10)
    penup()
    goto(xpos, ypos)
    pendown()
    dot(size, "white")


for x in range(100):



done()
