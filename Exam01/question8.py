from swampy.TurtleWorld import *
import math

def star_draw(turtle, length):
	fd(turtle, length)
	lt(turtle, 72)
	fd(turtle, length)
	rt(turtle, 144)

def star(turtle, length):
	star_draw(turtle, length)
	star_draw(turtle, length)
	star_draw(turtle, length)
	star_draw(turtle, length)
	star_draw(turtle, length)

def polyline(turtle, numberofmoves, length, angle):

	""" Poly line takes the turtle, the number of moves, 
	the length of each move and the angle that the turtle should
	turn at the end of each move and prints the turtle's movement """
	
	turtle.delay=0.01
	for i in range (numberofmoves):
		fd(turtle, length)
		rt(turtle, angle)

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


def circle_star(turtle, length):
	star(turtle, length)
	star_draw(turtle, length)
	lt(turtle, 72)
	circle(turtle, 1.42*length)

world=TurtleWorld() #Creates the world from TurtleWorld
bob=Turtle() #Creates the turtle object
bob.delay=0 #Changes the delay to 0 so that the turtle object draws faster

circle_star(bob, 100) #Calls dragon_start function to draw the curve

wait_for_user() #Holds the window open when the drawing is done