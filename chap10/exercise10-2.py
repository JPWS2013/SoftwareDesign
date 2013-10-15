def cumulative_sum(numlist):

	""""
	Takes a list of numbers and sums each element cumulatively and shows the result of each sums'

	numlist: Must be a list of numbers; No nesting allowed

	Returns a new list with each element being the cumulative sum of the previous elements of the original list
	"""
	incrementor=0
	cumulList=[]

	for eachNum in numlist:
		newTerm=incrementor + eachNum
		cumulList.append(newTerm)
		incrementor=newTerm

	return cumulList

numlist=[1,5,8,7,9,6]

print cumulative_sum(numlist)