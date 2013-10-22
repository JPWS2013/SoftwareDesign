def make_word_list():
    """Reads lines from a file and builds a list using append.

    returns: list of strings
    """
    t = []
    
    for line in open('words.txt'):
        word=line.strip()

        t.append(word)

    return t

memo={}

def generate_children(wordlist, word):
	children=[]

	if word in memo:
		return memo[word]

	for i in range(len(word)):
		newWord=word[:i] + word[i+1:]

		if newWord in wordlist:
			children.append(newWord)

		elif newWord.lower()=='i' or newWord.lower()=='a':
			children.append(newWord)

	memo[word]=children

	return children

def sub_child_gen(wordlist, children):

	if len(children) != 0:
		subchildren=[]
		for eachChild in children:
			subchildren=subchildren + generate_children(wordlist, eachChild)
		uniqueSubChildren=[]

		for eachSubChild in subchildren:
			if eachSubChild not in uniqueSubChildren:
				uniqueSubChildren.append(eachSubChild)

		return uniqueSubChildren

	else:
		return []

def is_reducible(wordlist, childList):
	
	child_list=sub_child_gen(wordlist, childList)

	if len(child_list)==1:
		return child_list[0].lower()=='a' or child_list[0].lower()=='i'

	elif len(child_list) != 0:
		return is_reducible(wordlist, child_list)

	else:
		return False

def longest_anagram(wordlist):
	anagram_list=[]
	for eachWord in wordlist:

		print eachWord

		#print is_reducible(wordlist, [eachWord])

		if is_reducible(wordlist, [eachWord]):
			anagram_list.append(eachWord)

	# sortedAnagrams=[]

	# for eachAnagram in anagram_list:
	# 	sortedAnagrams.append((len(eachAnagram), eachAnagram))

	# sortedAnagrams.sort()

	return anagram_list#sortedAnagrams[-1]

wordlist=make_word_list()

#print generate_children(wordlist, 'it')

#print longest_anagram(wordlist)
#wordlist=make_word_list()

#print generate_children(wordlist, 'it')

print is_reducible(wordlist, ['tree'])
#print memo