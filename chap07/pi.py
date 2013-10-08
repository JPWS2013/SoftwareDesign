import math

def estimate_pi():

	""" 
	Computes the approximate value of pi using an infinite series formulation by Srinivasa Ramanujan

	More about what this function does: It takes no arguments and returns the approximate value of pi

	Returns the approximate value of pi
	"""

	result = 1
	summation = 0
	k = 0.0

	while abs(result) > (10 ** (-15)):

		result1 = (math.factorial(4.0 * k)) * (1103.0 + (26390.0 * k))
		result2 = ((math.factorial(k)) ** 4.0) * (396.0 ** (4.0 * k))
		result = float(result1 / result2)

		summation=summation + result
		k += 1

	one_pi=((2.0 * float(math.sqrt(2.0))) / 9801.0) * summation

	return 1 / one_pi

print estimate_pi()