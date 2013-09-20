""" 
Solution to an exercise in Think Python.

Author: Justin Poh
"""

def grid(rows, columns):

	r='+ - - - - '
	c='|         '

	fullR=r*columns+'+\n'
	fullC=c*(columns+1)+'\n'

	grid=(fullR+(fullC*4))*rows + fullR

	print grid

grid(5,5)