from swampy.TurtleWorld import *

""" Module that provides functions that draw koch curves

Author: Justin Poh
"""

def draw(t, length, n):
	if n == 0:
		return
	angle = 50
	t.delay=0.01
	fd(t, length*n)
	lt(t, angle)

	draw(t, length, n-1)
	
	rt(t, 2*angle)
	
	draw(t, length, n-1)
	
	lt(t, angle)
	bk(t, length*n)


def koch(turtle, x):

	""" Draws a koch curve of length x

	More information about what this function does:

	turtle: must be a turtle object defined in TurtleWorld
	x: the length of the koch curve; Must be an integer """

	if x<3:
		fd(turtle, x)
		return

	koch(turtle, x/3.0)
	lt(turtle, 60)
	koch(turtle, x/3.0)
	rt(turtle, 120)
	koch(turtle, x/3.0)
	lt(turtle, 60)
	koch(turtle, x/3.0)

def snowflake(turtle, x):

	""" Draws a snowflake pattern using a series of koch curves 

	More information about what this function does:

	turtle: must be a turtle object defined in TurtleWorld
	x: length of each koch curve used to form the snowflake pattern; must be an integer """

	koch(turtle, x)
	rt(turtle, 120)
	koch(turtle, x)
	rt(turtle, 120)
	koch(turtle, x)

def general_koch(turtle, x, angle):

	""" Draws a Cesaro fractal (variation on koch curve) using a given length and turn angle 

	More information about what this function does:

	turtle: must be a turtle object defined in TurtleWorld
	x: the length of the koch curve; Must be an integer
	angle: Must be between 60 and 90 degrees """

	if x<3:
		fd(turtle, x)
		return

	general_koch(turtle, x/3.0, angle)
	lt(turtle, angle)
	general_koch(turtle, x/3.0, angle)
	rt(turtle, 2*angle)
	general_koch(turtle, x/3.0, angle)
	lt(turtle, angle)
	general_koch(turtle, x/3.0, angle)

world=TurtleWorld() # Creates the world from TurtleWorld
bob=Turtle() #Creates the turtle object from TurtleWorld
bob.delay=0 #Changes the delay to 0 so that the turtle moves faster when drawing

#draw(bob, 10, 10)
#koch(bob, 300) #Draws a koch curve using the above defined koch function
#snowflake(bob, 300) #Draws a snowflake using the above defined koch function
general_koch(bob, 1000, 85.0)

wait_for_user()