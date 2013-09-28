from swampy.TurtleWorld import *

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

	koch(turtle, x)
	rt(turtle, 120)
	koch(turtle, x)
	rt(turtle, 120)
	koch(turtle, x)

world=TurtleWorld()
bob=Turtle()
bob.delay=0

#koch(bob, 100)
snowflake(bob, 300)

wait_for_user()