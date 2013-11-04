def add_to_markov_dict(d, prefix, suffix):
	if prefix in d:
		d[prefix].append(suffix)

	else:
		d[prefix]=[suffix]

def invert_markov_dict(d):
	phrase_list=[]
	newD={}

	for eachPrefix in d:
		possibleSuffix=d[eachPrefix]
		for eachpossible in possibleSuffix:
			phrase=[eachPrefix[0], eachPrefix[1],eachpossible]
			phrase_list.append(phrase)
	
	for eachPhrase in phrase_list:
		newPrefix=(eachPhrase[1], eachPhrase[2])
		newSuffix=eachPhrase[0]
		add_to_markov_dict(newD, newPrefix, newSuffix)

	return newD

d={}
prefix='never', 'gonna'
for suffix in ['give', 'let', 'run', 'make', 'say', 'tell']:
	add_to_markov_dict(d, prefix, suffix)

flip=invert_markov_dict(d)

print flip
print d