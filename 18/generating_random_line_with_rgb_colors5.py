import turtle as t
import random
from turtle import Screen
johnny = t.Turtle()
t.colormode(255) # refer how rbg colours are working
directions = [0, 90, 180, 270]
def random_color(): # this funcion is the define the rgb color.
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colours = (r,g,b) # tuple
    return colours

johnny.pensize(10)

for i in range(200):
    johnny.color(random_color())
    johnny.forward(50)
    johnny.setheading(random.choice(directions))
    johnny.speed(10) # or we can type this as johnny.speed("fastest") or something like that. Bcoz it was defined, check the documentation

    
screen = Screen()
screen.exitonclick()