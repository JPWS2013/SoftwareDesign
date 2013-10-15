def nested_sum(numlist):

	"""
	Takes a list of numbers and returns the sum of all elements in the list

	numlist: must be a list of integers; May contain any number of nested list

	Returns the cumulative sum of all integers in a list

	"""

	accumulator=0

	for eachItem in numlist:

		if type(eachItem)== list:
			current_sum=nested_sum(eachItem)
			accumulator = accumulator + current_sum

		else:
			accumulator = accumulator + eachItem

	return accumulator

numlist=[1,2,[1,2,[1,2,[1,2,[1,2,3],4,5,6]]]]

print nested_sum(numlist)