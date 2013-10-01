from swampy.TurtleWorld import *

""" Module that provides functions that draw dragon curves

Credit: This code was written using the L-system from http://en.wikipedia.org/wiki/L-system#Example_6:_Dragon_curve;
        This code was also written with the help of Julian(ninja).

Author: Justin Poh
"""

def dragon_start(turtle, n, fd_len):

    """ Draws a level n dragon curve

    More information about what this function does:

    turtle: Must be a turtle object from TurtleWorld
    n: must be an integer number
    fd_len: the length of the forward movement; Must be a number """

    angle=90

    fd(turtle, fd_len)
    dragon_x(turtle, n, fd_len)

def dragon_x(turtle, n, fd_len):

    """ Draws the forward version of the dragon curve
    
    More information about what this function does:

    This function is part of a recursive set of functions beginning with the function "dragon_start"
    turtle: Must be a turtle object from TurtleWorld
    n: must be an integer number
    fd_len: the length of the forward movement; Must be a number """

    angle=90
    
    if n==0:
        return
    
    dragon_x(turtle, n-1, fd_len)
    rt(turtle, angle)
    dragon_y(turtle, n-1, fd_len)
    fd(turtle, fd_len)

def dragon_y(turtle, n, fd_len):

    """ Draws the reverse version of the dragon curve
    
    More information about what this function does:

    This function is part of a recursive set of functions beginning with the function "dragon_start"
    turtle: Must be a turtle object from TurtleWorld
    n: must be an integer number
    fd_len: the length of the forward movement; Must be a number """

    angle=90

    if n==0:
        return

    fd(turtle, fd_len)
    dragon_x(turtle, n-1, fd_len)

    lt(turtle, angle)
    dragon_y(turtle, n-1, fd_len)



world=TurtleWorld() #Creates the world from TurtleWorld
bob=Turtle() #Creates the turtle object
bob.delay=0 #Changes the delay to 0 so that the turtle object draws faster

dragon_start(bob, 10, 10) #Calls dragon_start function to draw the curve

wait_for_user() #Holds the window open when the drawing is done