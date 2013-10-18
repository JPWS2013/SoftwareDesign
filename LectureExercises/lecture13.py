def has_duplicates(t):
	return len(t)!=len(set(t))

def list_intersection(t1, t2):
	return list(set(t1).intersection(set(t2)))

def uses_only(word, s):
	return set(word).issubset(s)

def avoids(word, s):
	return set(word).isdisjoint(s)

t1=[1,2,2]
t2=[1,3,2,2]

#print has_duplicates(t1)

#print list_intersection(t1, t2)

word='testaaa'
case='uyzra'

#print uses_only(word, case)

print avoids(word, case)