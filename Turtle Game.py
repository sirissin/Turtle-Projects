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

done()
