def list_intersection(t1, t2):
	
	intersection=[]

	for element in t1:
		if element in t2:
			intersection.append(element)

	return intersection

def sorted_keys(d):
	allKeys=d.keys()

	allKeys.sort()

	return allKeys

#print list_intersection([1,3,5,7, 2,4,6,8,0,10,11], [3,2,1])

#d={'uno':'one', 'dos':'two', 'tres':'three', 'argh':'argh'}
#print sorted_keys(d)