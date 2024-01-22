from turtle import *

#Balloon parameters
diameter = 40
pop_diameter = 100

#Draw the balloon
def draw_balloon():
    color("red")
    dot(diameter)


def inflate_balloon():
    global diameter
    diameter = diameter + 10
    draw_balloon()


draw_balloon()
inflate_balloon()
Screen().exitonclick()