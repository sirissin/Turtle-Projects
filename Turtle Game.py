from turtle import *


# Screen Properties
bgcolor("#FA9A43")

speed(0)
move_distance = 20

# Getting to the starting point of the Ocean
penup()
goto(100, 200)
pendown()

# Create the Ocean
color("#03A0FA")
begin_fill()
goto(300, 200)
goto(300, -200)
goto(100, -200)
end_fill()
penup()


goto(-200, 0)
color("green")
shape("turtle")


# Created the Functions for moving and rotating the Turtle
def move_up():
    setheading(90)
    forward(move_distance)


def move_down():
    setheading(270)
    forward(move_distance)


def move_left():
    setheading(180)
    forward(move_distance)


def move_right():
    setheading(0)
    forward(move_distance)


# Functionality for moving the Turtle by pressing keys
onkey(move_up, key="Up")
onkey(move_down, key="Down")
onkey(move_left, key="Left")
onkey(move_right, key="Right")

listen()
done()
