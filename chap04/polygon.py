from swampy.TurtleWorld import *
import math

def polyline(turtle, numberofmoves, length, angle):

	""" Poly line takes the turtle, the number of moves, 
	the length of each move and the angle that the turtle should
	turn at the end of each move and prints the turtle's movement """
	
	turtle.delay=0.01
	for i in range (numberofmoves):
		fd(turtle, length)
		lt(turtle, angle)

def square(turtle, length):

	""" Square takes the length of the sides of the square and 
	prints the turtle's movement"""

	polyline(turtle, 4, length, 90)

def polygon(turtle, sides, length):

	""" Polygon takes the turtle, number of 
	sides and the desired length of each side and prints the turtle's
	path """

	angle=360/sides
	polyline(turtle, sides, length, angle)

def circle(turtle, radius):

	""" Circle takes the number of """
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

	lt(turtle, angle_to_move/2)	
	polyline(turtle, numberofmoves, length, angle_to_move)




world=TurtleWorld()
bob=Turtle()
print bob

#square(bob,100)
#circle(bob, 100)
arc(bob, 100, 90)
for i in range (1,20):
	lt(bob, 98)
	arc(bob, 100, 180)


wait_for_user()