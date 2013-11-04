def binomial_coeff(n,k):
	memo={}

	if k==0:
		return 1

	if n==0:
		return 0

	try:
		return memo[n,k]

	except KeyError:
		res=binomial_coeff(n-1,k) + binomial_coeff(n-1,k-1)
		memo[n,k] = res

	return memo[n,k]

def make_word_set():
	s=set()

	fp=open('fakewords.txt')
	for word in fp:
		cleanWord=word.strip().lower() 
		s.add(cleanWord)

	return s


def children(word, word_set):
	res=[]

	for i in range(len(word)):
		child=word[:i]+word[i+1:]
		print child
		if child in word_set:
			res.append(child)

	return res

#print binomial_coeff(3,2)

print make_word_set()

# print children('ping', wordset)