from swampy.Lumpy import Lumpy

lumpy=Lumpy()

def date_strings(datestring):
	res=[]
	sortedT=[]

	for eachDate in datestring:
		splitlist=eachDate.split('/')
		splitTuple=(splitlist[2], splitlist[1], splitlist[0], eachDate)
		sortedT.append(splitTuple)
	
	sortedT.sort()

	for eachDateTuple in sortedT:
		res.append(eachDateTuple[3])

	lumpy.object_diagram()

	return res

dates=['03/02/1997', '04/03/1993', '05/06/1991', '06/06/1993']

print date_strings(dates)