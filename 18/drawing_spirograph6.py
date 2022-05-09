import turtle as t
import random

def random_color(): # this funcion is the define the rgb color.
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colour = (r,g,b) # tuple
    return colour


def spirograph(sizeofgap,direction):
    for i in range(360//sizeofgap):
        jilly.setheading(direction)
        jilly.speed(15)
        jilly.color(random_color())
        jilly.circle(100)
        direction += sizeofgap


jilly = t.Turtle()
t.colormode(255) # refer how rbg colours are working
direction = 0
jilly.pensize(2)

sizeofgap = random.randint(5,15) # making the size of the gap between circles as random


spirograph(sizeofgap, direction)


screen = t.Screen()
screen = t.exitonclick()