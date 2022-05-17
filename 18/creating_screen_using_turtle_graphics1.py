# in this program we are gonna create the blank screen using the turtle graphics
# and making the turtle move forward and turn right by 90 degree.

from turtle import Turtle, Screen
turtle_name = Turtle()
turtle_name.shape("circle") # changing the shape to circle
turtle_name.color("red") # changing color to red

turtle_name.forward(100) # making the circle move forward by 100
turtle_name.right(90) # rotating 90 degrees to the right

screen = Screen() # creating the screen
screen.exitonclick() # making the screen exit on click.
