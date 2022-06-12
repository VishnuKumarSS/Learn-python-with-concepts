from turtle import Screen, Turtle

turtle = Turtle()
screen = Screen()


def move_forward():
    turtle.forward(20)
def move_backward():
    turtle.backward(20)
def turn_left():
    new_heading = turtle.heading() + 20
    turtle.setheading(new_heading)
def turn_right():
    new_heading = turtle.heading() - 20
    turtle.setheading(new_heading)
def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen() 
screen.onkey(fun= move_forward, key="w")
screen.onkey(fun= move_backward, key="s")
screen.onkey(fun= turn_left, key="a")
screen.onkey(fun= turn_right, key="d")
screen.onkey(fun= clear, key="c")

screen.exitonclick()

