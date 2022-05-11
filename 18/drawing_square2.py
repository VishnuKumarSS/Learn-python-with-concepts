# drawing the square using turtle graphics
from turtle import Turtle, Screen

turtle_name = Turtle()
for i in range(4):
    turtle_name.forward(100)
    turtle_name.right(90)

screen = Screen()
screen.exitonclick()