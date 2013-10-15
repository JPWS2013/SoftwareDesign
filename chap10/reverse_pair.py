import bisect

def make_word_list():
    """Reads lines from a file and builds a list using append.

    returns: list of strings
    """
    t = []
    
    for line in open('words.txt'):
        word=line.strip()

        t.append(word)

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

def reverse_pair(wordlist, word):

	"""
	Checks if a word is a reverse pair with another word in the list

	wordlist: must be a list object consisting of elements that are all strings
	word: must be a string object

	 
	"""

	reverseWord=word[::-1]

	if is_in_list(wordlist, reverseWord):
		return [word, reverseWord]
	else:
		return False


wordlist=make_word_list()
reversePairs=[]

for eachWord in wordlist:
	result=reverse_pair(wordlist, eachWord)
	if result !=False:
		reversePairs.append(result[0])
		reversePairs.append(result[1])

print reversePairs