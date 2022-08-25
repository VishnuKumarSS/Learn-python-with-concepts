# 1. CREATING SNAKE BODY


from turtle import Turtle, Screen, width
screen = Screen()
screen.setup(width=800, height=600)
# here height = y = 300,-300 ----- width = x=400,-400
screen.title("Snake Game - Vishnu")
screen.bgcolor("black") # setting background color as black.


positions =[(0,0),(-20,0),(-40,0)] # list of position values using tuples.
for pos in positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(pos) # here the values of x and y inside the goto function set by looping through the positions list that we have created.





screen.exitonclick()
