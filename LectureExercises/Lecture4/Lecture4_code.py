import math

def sum_range(n):
	testType=type(n)

	if testType!=int:
		if testType==float:
			n=int(n)

		else:
			print "You have entered an invalid value"


	if type(n)==int or type(n)==float:

		return sum(range(n))


def sum_squares(a,b):
	
	if type(a)==int or type(a)==float and type(b)==int or type(b)==float:

		return (a**2+b**2)

	else:
		print "You have entered an invalid value"


def hypotenuse(a, b):

	if type(a)==int or type(a)==float and type(b)==int or type(b)==float:

		return math.sqrt((a**2+b**2))

	else:
		print "You have entered an invalid value"

def right_justify(string):

	counter=0

	length=len(string)

	numSpaces=70-length

	for testrange in range(numSpaces):
		print '',

	print string

def do_twice(f, argument):
	f(argument)
	f(argument)

def print_spam(string):
	print string

def do_four(f, argument):
	do_twice(f, argument)
	do_twice(f, argument)

#print sum_range('woot') #Exerccise 1


#print sum_squares(3,4) #Exercise 2

#print hypotenuse(3,4) #Exercise 3

#right_justify('Allen') #Exercise 4

do_four(print_spam, 'I AM HERE!!') #Exercise 5