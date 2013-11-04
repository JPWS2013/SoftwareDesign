def sorted_names(t):
	tuple_list=[]
	res=[]

	for eachName in t:
		nameParts=eachName.split(' ')

		last=nameParts[-1]
		given=''

		for i in range(len(nameParts)-1):
			given=given+str(nameParts[i])+' '
		
		name_tuple=(last,given)
		tuple_list.append(name_tuple)

	tuple_list.sort()

	for last,given in tuple_list:
		name=given+last
		res.append(name)


	return res




names=['Wilhelm Grimm', 'Thomas Crofton Croker', 'Jacob Grimm', 'Justin Wei Siang Poh']

print sorted_names(names)