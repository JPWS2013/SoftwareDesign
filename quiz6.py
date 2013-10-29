memo={}

def binomial_coeff(n,k):

	if k==0:
	 	return 1

	if n==0:
	 	return 0

	if (n, k) in memo:
		return memo[n, k]

	res=binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)
	memo[(n,k)]=res
	return res

def caseless_sorted(names):
	tuplelist=[]
	res=[]

	for name in names:
		tuplelist.append((name.lower(), name))


	tuplelist.sort()

	for key,value in tuplelist:
		res.append(value)

	return res

names=['abc1', 'ABC2', 'aBc3']

#print caseless_sorted(names)


print binomial_coeff(5,3)
print memo