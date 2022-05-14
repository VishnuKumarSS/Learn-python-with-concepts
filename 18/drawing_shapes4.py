# drawing the triangle, square, pentagon, hexagon, heptagon, octagon, nanogon, decagon using turtle graphics
from turtle import Turtle, Screen
import random
turtle_name = Turtle()


colours = ["red","blue","green","yellow","brown","pink","orange","purple"]
# dividing the 360 degree with the shapes sides.
# eg.
# triangle has 3 sides, so 360 / 3 is 120. the angle of triangle is 120 degree
# same as triangle,for all the shapes.
# square has 4 sides, so 360 / 4 is 90. the angle of square is 90 degree.
# so,
for i in range(3,11): # this loops starts with 3 (i.e) for triangle untill decagon which is 10.

    turtle_name.color(random.choice(colours))
    for j in range(i):
        turtle_name.forward(100) # moving forward 30
        turtle_name.right(360/i)
# the above loop make the all shapes triangle, square, pentagon, hexagon, heptagon, octagon, nanogon, decagon

screen = Screen()
screen.exitonclick()