def cumulative_sum(numlist):
	incrementor=0
	cumulList=[]

	for eachNum in numlist:
		newTerm=incrementor + eachNum
		cumulList.append(newTerm)
		incrementor=newTerm

	return cumulList

numlist=[1,5,8,7,9,6]

print cumulative_sum(numlist)