from swampy.TurtleWorld import *

def square(turtle, length):
	for i in range (4):
		fd(turtle, length)
		lt(turtle)

def polygon(turtle, sides, length):
	for i in range (sides):
		angle=360/sides
		fd(turtle, length)
		lt(turtle, angle)

def circle(turtle, radius):

	fd (turtle, radius)
	lt(turtle, 90)
	
	for i in range (360):
		
		fd(turtle, length)
		lt(turtle, )

world=TurtleWorld()
bob=Turtle()
print bob

polygon(bob, 5, 50)


wait_for_user()