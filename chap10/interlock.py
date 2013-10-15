import bisect
import time

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

def interlock(wordlist, word):

	firstWord=word[::2]
	secondWord=word[1::2]

	return is_in_list(wordlist, firstWord) and is_in_list(wordlist, secondWord)

def interlock_general(wordlist, word, n=3):

	sep_word_list=[]

	for i in range(n):
		sep_word_list.append(word[i::n])

	for eachSepWord in sep_word_list:
		if not is_in_list(wordlist, eachSepWord):
			return False

	return True


wordlist=make_word_list()
testlist=[]

# for eachWord in wordlist:
# 	if interlock(wordlist, eachWord):
# 		testlist.append(eachWord)
# 		print eachWord, ' ', eachWord[::2], ' ', eachWord[1::2]


for eachWord in wordlist:
	if interlock_general(wordlist, eachWord):
		testlist.append(eachWord)
		#print eachWord, ' ', eachWord[::3], ' ', eachWord[1::3], eachWord[2::3]

print len(testlist)