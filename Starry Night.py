from turtle import *
from random import *

#Screen properties
title("Starry Night")
bgcolor('black')
hideturtle()

width = window_width()
height = window_height()

#Draw Speed
speed(0)


#Draw a Star
def draw_star(xpos, ypos):
    size = randrange(4, 10)
    penup()
    goto(xpos, ypos)
    pendown()
    dot(size, "white")


#Loop to make 100 stars
for x in range(100):
    xpos = randrange(round(-width / 2), round(width / 2))
    ypos = randrange(round(-height / 2), round(height / 2))
    draw_star(xpos, ypos)


done()
