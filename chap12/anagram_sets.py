def make_word_list():
    """Reads lines from a file and builds a list using append.

    returns: list of strings
    """
    t = []
    
    for line in open('words.txt'):
        word=line.strip()

        t.append(word)

    return t

def anagrams(wordlist):
	anagrams=dict()

	for eachWord in wordlist:
		charList=list(eachWord)
		charList.sort()
		charList=tuple(charList)

		if charList in anagrams:
			anagrams[charList].append(eachWord)

		else: 
			anagrams[charList]=[eachWord]

	return anagrams

def print_in_order(anagramlist):

	orderedList=[]

	for charList, wordList in anagramlist.items():

		if len(wordList)>1:
			orderedList.append((len(wordList), wordList))

	orderedList.sort()

	for eachTuple in orderedList:
		print eachTuple

def best_for_bingo(anagramlist, n):
	orderedList=[]

	for charList, wordList in anagramlist.items():
		if len(charList)==n:
			orderedList.append((len(wordList), wordList))

	orderedList.sort()

	bestLetters=orderedList[-1][1][0] #Retreives the letters it would take to make any of the words in the tuple

	return list(bestLetters)


wordlist=make_word_list()

#fakewordlist=['deltas', 'desalt','lasted', 'salted', 'slated', 'staled', 'retainers', 'ternaries', 'generating', 'greatening', 'resmelts', 'smelters', 'termless']
result= anagrams(wordlist)

#print_in_order(result)

print best_for_bingo(result, 8)