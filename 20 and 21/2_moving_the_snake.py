# 2. Moving the snake

from turtle import Turtle, Screen, width
import time

screen = Screen()
screen.setup(width=800, height=600)
# here height = y = 300,-300 ----- width = x=400,-400
screen.title("Snake Game - Vishnu")
screen.bgcolor("black") # setting background color as black.
screen.tracer(0) # it will stop the screen, and do not refresh until the update method is called.

positions =[(0,0),(-20,0),(-40,0)] # list of position values using tuples.

# 1.create snake
segments = [] # body of the snake is stored as the squares in this list.
for pos in positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup() # to not to make the line   
    new_segment.goto(pos) # here the values of x and y inside the goto function set by looping through the positions list that we have created.
    segments.append(new_segment)

# 2.move snake
move = True
while move:
    screen.update() # here only the screen gets updated after tracer is called. The above code doesn't do anything until this update is called. (i.e) doesn't show anything on the screen until this method is called.
    time.sleep(0.1) # this adds 0.1 second delay to each segment moves.
    # for seg in segments:
    #     seg.forward(20)
    for seg_num in range(len(segments) - 1 , 0 ,-1):  # range(start = len(segments)-1, stop = 0, step = -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x,new_y)
    segments[0].forward(20)
















screen.exitonclick()
