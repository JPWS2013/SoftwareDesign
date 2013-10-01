from swampy.TurtleWorld import *

""" Draws a dragon curve of given level n using TurtleWorld

More about what this function does:

turtle: the turtle object created using TurtleWorld from swampy
n: the level of the dragon curve
fd_len: the length that the turtle will travel each time

Credit: This code was written using the L-system from http://en.wikipedia.org/wiki/L-system#Example_6:_Dragon_curve;
This code was also written with the help of Julian(ninja).

"""

def dragon_start(turtle, n, fd_len):
    angle=90
    fd(turtle, fd_len)
    dragon_x(turtle, n, fd_len)

def dragon_x(turtle, n, fd_len):
    angle=90
    
    if n==0:
        return
    
    dragon_x(turtle, n-1, fd_len)
    rt(turtle, angle)
    dragon_y(turtle, n-1, fd_len)
    fd(turtle, fd_len)

def dragon_y(turtle, n, fd_len):

    angle=90

    if n==0:
        return

    fd(turtle, fd_len)
    dragon_x(turtle, n-1, fd_len)

    lt(turtle, angle)
    dragon_y(turtle, n-1, fd_len)

world=TurtleWorld()
bob=Turtle()
bob.delay=0

dragon_start(bob, 10, 30)

wait_for_user()