import bisect

def make_word_list1():
    """Reads lines from a file and builds a list using append.

    returns: list of strings
    """
    t = []
    
    for line in open('words.txt'):
        word=line.strip()

        t.append(word)

    return t

def is_in_list(wordlist, word):
	i=bisect.bisect_left(wordlist, word)

	if i != len(wordlist) and wordlist[i]==word:
		return True
	else:
		return False

wordlist=make_word_list1()

# wordlist=['children', 'cow', 'tongue', 'kid', 'hopper']

# wordlist.sort()

print is_in_list(wordlist, 'zzzzzzzzzzzzzzzzz')