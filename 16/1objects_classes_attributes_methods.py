# OBJECTS, CLASSES, ATTRIBUTES, METHODS


# here we are importing inbuilt turtle module
# to know everything about the turtle module, visit
# https://docs.python.org/3/library/turtle.html

# to know to colour code , visit
# https://cs111.wellesley.edu/labs/lab01/colors

from turtle import Screen, Turtle  # # here Turtle is a class in turtle module

timmy = Turtle() # creating a new object called timmy from the blueprint (i.e) class

# we should use paranthesis to initialize/construct an object.
# and we are assigning that Turtle class to the variable called timmy. 
# This means that variable timmy is the object
print(timmy) # it shows the object location only if we run


# Here we are calling methods that are associated with the objects
 
timmy.shape("turtle") # it makes the arrow on the screen to look like turtle # it's prebuild in the turtle module
timmy.color("blue") # here we are colouring the turtle
# here shape and color is the functions inside the turtle module
# timmy.position('up')
timmy.forward(70) # here turtle moves forward 70 step
timmy.circle(100) # here turtle makes a circle of 100 steps


my_screen = Screen() # here we are creating the object called my_screen from the blueprint (i.e) class.

# here below, my_screen is the object , canvheight is the attibutes of the object my_screen 
print(my_screen.canvheight)  # 300 is set as default

my_screen.canvheight = 500 # here canvheight is the attribute (i.e) variable, 
# so we cannot pass the arguments to the variable, we can only assign the values to it.

print(my_screen.canvheight) # here it will show that the height as 400

my_screen.exitonclick() # here exitonclick is the function 
# what it do is it makes the screen to stay until the click on the screen is detected.
