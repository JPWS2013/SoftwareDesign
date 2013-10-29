import random 

def make_histogram(wordlist):
    """Make a map from words to number of times they appear in wordlist.

    wordlist: list of strings

    Returns: map from word to frequency
    """
    hist = {}
    for word in wordlist:
        hist[word] = hist.get(word, 0) + 1
    
    return hist

def random_word(hist):

	t=[]

	for word, freq in hist.items():
		t.extend([word]*freq)

	return random.choice(t) 

words={'three': 2, 'ten': 1, 'tree': 1}
res=[]
for i in range(12):
	res.append(random_word(words))

print make_histogram(res)