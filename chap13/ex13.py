import string
import bisect

def clean_line(fileline):
    fileline=fileline.replace('-', ' ')
    temp_wordlist=fileline.split(' ')
    out_temp_wordlist=[]
    
    for i in range(len(temp_wordlist)):

        if temp_wordlist[i]=='':
            continue
        else:
            holder=temp_wordlist[i]

            holder=holder.strip(string.whitespace)
            holder=holder.strip('\xef\xbb\xbf')
            holder=holder.strip(string.punctuation)
            holder=holder.lower()

            out_temp_wordlist.append(holder)

    return out_temp_wordlist

def read_gutenberg(filename, booktitle):
    startofbook=False
    allWords=[]

    clean_booktitle=clean_line(booktitle)

    for line in open(filename):
        test_line=clean_line(line)

        if test_line==clean_booktitle and line.isupper():
            startofbook=True

        if startofbook==True:

            temp_holder=clean_line(line)

            if temp_holder != ['']:
                allWords=allWords+clean_line(line)

    return allWords

def make_histogram(wordlist):
    """Make a map from words to number of times they appear in wordlist.

    wordlist: list of strings

    Returns: map from word to frequency
    """
    hist = {}
    for word in wordlist:
        hist[word] = hist.get(word, 0) + 1
    
    return hist

def most_frequent(wordDict, n):
    t=[]

    for word, frequency in wordDict.items():
        t.append((frequency, word))

    t.sort(reverse=True)

    return t[:(n+1)]

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

def not_words(wordlist, wordDict):

    notwords=[]

    allWords=wordDict.keys()

    for eachWord in allWords:
        if not is_in_list(wordlist, eachWord):
            notwords.append(eachWord)

    return notwords

# allWords=[]

# for line in open('fakewords.txt'):
#   #print line
#   allWords = allWords + clean_line(line)

#print allWords
wordlist=make_word_list()

listresult = read_gutenberg('pg1118.txt', 'much ado about nothing')

dictresult = make_histogram(listresult)

listofnotwords=not_words(wordlist, dictresult)

print listofnotwords
#print most_frequent(dictresult, 20)

#allkeys=dictresult.keys()

#print dictresult