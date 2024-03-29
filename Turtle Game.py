from turtle import *


# Screen Properties
title("Turtle Game")
height = 400
width = 620
setup(width, height)
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
    check_goal()


def move_down():
    setheading(270)
    forward(move_distance)
    check_goal()


def move_left():
    setheading(180)
    forward(move_distance)
    check_goal()


def move_right():
    setheading(0)
    forward(move_distance)
    check_goal()


# Checking for a win condition
def check_goal():
    if xcor() > 100:
        hideturtle()
        color("white")
        write("YOU WIN!", font=("Arial", 24, "bold"))

        # Reset key functionality after win condition
        onkey(None, key="Up")
        onkey(None, key="Down")
        onkey(None, key="Left")
        onkey(None, key="Right")


# Functionality for moving the Turtle by pressing keys
onkey(move_up, key="Up")
onkey(move_down, key="Down")
onkey(move_left, key="Left")
onkey(move_right, key="Right")

listen()
done()
