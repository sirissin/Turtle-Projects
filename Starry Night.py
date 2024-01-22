from turtle import *

#Screen properties
title("Starry Night")
bgcolor('black')
hideturtle()


#Draw a Star
def draw_star(xpos, ypos):
    penup()
    goto(xpos, ypos)
    pendown()
    dot(20, "white")


draw_star(0,0)


done()
