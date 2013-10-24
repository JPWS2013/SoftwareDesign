def make_word_list():
    """Reads lines from a file and builds a list using append.

    returns: list of strings
    """
    t = dict()
    
    for line in open('words.txt'):
        word=line.strip()

        t[word]=word

    return t

memo={}
memo['']=['']

def children(wordDict, word):

	childList=[]

	if word in memo:
		return memo[word]

	for i in range(len(word)):
		newWord=word[:i]+word[i+1:]
		
		if newWord in wordDict:
			childList.append(newWord)

		elif newWord=='i' or newWord =='a' or newWord=='':
			childList.append(newWord)
	

	memo[word]=childList

	return childList

def is_reducible(wordDict, word):
	result = []

	if word in memo:
		return memo[word]

	for eachChild in children(wordDict, word):
		children_list=is_reducible(wordDict, eachChild)

		if children_list:
			result.append(eachChild)

	return result


def find_all_reducible(wordDict):
	reducibles=[]
	for eachWord in wordDict:
		#print eachWord
		if is_reducible(wordDict, eachWord):
			reducibles.append(eachWord)

	return reducibles

def print_longest(wordDict):
	t=[]

	all_reducible=find_all_reducible(wordDict)

	for eachReducible in all_reducible:
		t.append((len(eachReducible), eachReducible))

	t.sort(reverse=True)

	print t[0:5]

wordDict=make_word_list()

#print_longest(wordDict)

#print is_reducible(wordDict, 'weakeners')
# fakewordDict=dict()
# fakewordDict['orange']=['orange']

print find_all_reducible(wordDict)

#print children(wordDict, '')

#print memo