import bisect

def rotate_word(s, order):
	"""
	Takes a string and a rotation number and rotates the string by the given amount

	More information about this function:

	s: Needs to be a string
	order: Needs to be an integer

	Returns the rotated string

	"""
	
	newString=''

	for eachChar in s:

		if eachChar.isupper():
			start_code=ord('A')
		elif eachChar.islower():
			start_code=ord('a')
		else:
			newString=newString+eachChar
			continue
		
		total_letters = 26

		startIndex = ord(eachChar)
		endIndex = ((startIndex - start_code + order) % total_letters) + start_code
		newString = newString + chr(endIndex)

	return newString

def make_word_list():
    """Reads lines from a file and builds a list using append.

    returns: list of strings
    """
    t = dict()
    
    for line in open('words.txt'):
        word=line.strip()

        t[word]=word

    return t

def is_in_list(wordlist, word):

	"""
	Checks if a word is in a word list

	wordlist: must be a list object consisting of elements that are all strings
	word: must be a string object

	Returns Boolean True or False values

	"""

	i=bisect.bisect_left(wordlist, word)

	if i != len(wordlist) and wordlist[i]==word:
		return True
	else:
		return False

def rotate_pairs(wordlist, testWord):
	testlist=[]

	for i in range(1,14):
		rotatedWord=rotate_word(testWord, i)
		if rotatedWord in wordlist:
			#print testWord, rotatedWord
			testlist.append(rotatedWord)

	return testlist

wordlist=make_word_list()

existinglist=[]

for eachWord in wordlist:
	#rotate_pairs(wordlist, eachWord)
	testedlist=rotate_pairs(wordlist, eachWord)
	existinglist=existinglist+testedlist

print len(existinglist)