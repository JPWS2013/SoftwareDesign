def remove_duplicates(origList):
	newlist=[]

	for eachElement in origList:
		anElement=eachElement
		
		if anElement not in newlist:
			newlist.append(eachElement)

	return newlist

original=[1,2,3,4, 3, 6, 10,5,6,7, 3, 1, 2]

unique=remove_duplicates(original)

print unique