from turtle import *

screen = Screen()
screen.bgcolor("black")

color("red")
begin_fill()
left(50)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)
end_fill()

penup()
goto(4, 90)
color("white")
write("I Love You", align="center", font=("Arial", 24, "bold"))
hideturtle()

done()