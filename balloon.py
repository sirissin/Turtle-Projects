from turtle import *
import random

#Screen Properties
title("Balloon Popper")
bgcolor("#ADD8E6")

#Balloon parameters
diameter = 40
pop_diameter = 100
#Range of colors for the balloons
color_wheel = ["red", "yellow", "blue", "green", "purple"]
#Simple counter to allow for different colored balloons after the first pop
counter = 0

hideturtle()


#Draw the balloon
def draw_balloon():
    if counter == 0:
        color('red')
    dot(diameter)


#Inflate the Balloon
def inflate_balloon():
    global diameter, counter
    diameter = diameter + 10
    draw_balloon()

    #Limit the balloon inflation and cause the Pop
    if diameter >= pop_diameter:
        clear()
        diameter = 40
        write('POP!', font=('Arial', 10, 'normal'))
        bal_col = random.choice(color_wheel)
        color(bal_col)
        counter += 1


draw_balloon()

#Use the up arrow key to inflate the balloon
onkey(inflate_balloon, "Up")
listen()

done()