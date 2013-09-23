from swampy.TurtleWorld import *
import math

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
	numberofmoves=40
	circumference=2*math.pi*radius
	length=circumference/numberofmoves
	turtle.delay=0.01
	polygon(turtle, numberofmoves, length)

def arc(turtle, radius, angle):
	distance_to_move=float(radius*math.radians(angle))
	numberofmoves=40
	length=float(distance_to_move/numberofmoves)
	turtle.delay=0.01
	angle_to_move=float(angle/numberofmoves)
	
	for i in range (numberofmoves):
		fd(turtle, length)
		lt(turtle, angle_to_move)

world=TurtleWorld()
bob=Turtle()
print bob

#square(bob,10)
#circle(bob, 10)
arc(bob, 100, 270)


wait_for_user()