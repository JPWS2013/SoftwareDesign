def most_frequent(s):
	letters=dict()
	reversedHistogram=[]
	finalresult=[]

	for c in s:
		letters[c]=letters.get(c, 0) + 1

	for letter, frequency in letters.items():
		reversedHistogram.append((frequency, letter))

	reversedHistogram.sort(reverse=True)

	for frequency, letter in reversedHistogram:
		finalresult.append(letter)

	return finalresult

def read_file(filename):
    """Returns the contents of a file as a string."""
    return open(filename).read()

#print most_frequent('test')

s = read_file('words.txt')
t = most_frequent(s)
for x in t:
    print x