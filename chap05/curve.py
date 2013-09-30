from swampy.TurtleWorld import *

""" Draws a dragon curve of given level n using TurtleWorld

More about what this function does:

turtle: the turtle object created using TurtleWorld from swampy
n: the level of the dragon curve
fd_len: the length that the turtle will travel each time

Credit: This code was modified from http://www.comscigate.com/cs/IntroSedgewick/20elements/27recursion/Dragon.java.html

"""

def reverse_curve(turtle, n, fd_len):
    angle=90

    if n==0:
        fd(turtle, fd_len)
        return

    else:
        curve(turtle, n-1, fd_len)
        lt(turtle, angle)
        reverse_curve(turtle, n-1, fd_len)

def curve(turtle, n, fd_len):

    angle=90

    if n==0:

        fd(turtle, fd_len)
        return

    else:
        curve(turtle, n-1, fd_len) #This will ensure that the first dragon curve element will always be a forward version
        rt(turtle, angle) #This will turn 90 degrees
        reverse_curve(turtle, n-1, fd_len) #Ensures that if the programme is at the base unit, it draws a line, if it is not at the base unit, it alternates between turning left and right (between calling curve and reverse_curve)

world=TurtleWorld()
bob=Turtle()
bob.delay=0

#koch(bob, 100)
curve(bob, 3, 30)

wait_for_user()