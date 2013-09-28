def is_divisible(a,b):

	""" Determines if two numbers are divisible or not

	More information about the function:

	a: Number to divide; Should be an integer
	b: Number to be divided by; Should also be an integer

	Returns True if the two numbers are divisible, returns false otherwise """

	if a%b==0:
		return True

	else:
		return False

def is_power(a,b): #Exercise 6.7

	""" Takes two arguments a and b and determines if a is a power of b

	More information about the function:

	a: should be an integer
	b: should be an integer

	Returns True if a is a power of b, returns False otherwise """

	if type(a)==float or type(b)==float:
		print "At least one of the numbers that you have provided will not work because it is not an integer"
		return False

	if a==1:
		return True

	if is_divisible(a,b):
		is_power(a/b, b)

	else:
		return False

	return True

def gcd(a,b):

	""" Determines the greatest common divisor (GCD) of two numbers

	More information about the function:

	a: Should be a number (either decimal or integer)
	b: Should be a number (either decimal or integer)

	Returns the GCD of the two numbers """

	if b==0:
		return a
	
	r=a%b

	if r==0:
		return b
	else:
		holder=gcd(b,r)
		return holder

print gcd(450.0, 100.0 )