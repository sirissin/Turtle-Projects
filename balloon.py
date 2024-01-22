from turtle import *

#Balloon parameters
diameter = 40
pop_diameter = 100


#Draw the balloon
def draw_balloon():
    color("red")
    dot(diameter)


#Inflate the Balloon
def inflate_balloon():
    global diameter
    diameter = diameter + 10
    draw_balloon()

    #Limit the balloon inflation and cause the Pop
    if diameter >= pop_diameter:
        clear()
        diameter = 40
        write('POP!')


draw_balloon()

#Use the up arrow key to inflate the balloon
onkey(inflate_balloon, "Up")
listen()

Screen().exitonclick()