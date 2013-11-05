def make_word_list():
    """Reads lines from a file and builds a list using append.

    returns: list of strings
    """
    t = []
    
    for line in open('words.txt'):
        word=line.strip()

        t.append(word)

    t.append('a')
    t.append('i')
    t.append('')

    return t

memo={'':['']}

def generate_children(word, wordlist):
    children=[]

    for i in range (len(word)):
        newWord=word[:i]+word[i+1:]

        if newWord in wordlist:
            children.append(newWord)

    return children

def is_reducible(word, wordlist):

    if word in memo:
        return memo[word]

    res=[]

    child_list=generate_children(word, wordlist)

    for eachWord in child_list:
        sub_child_list= is_reducible(eachWord, wordlist)
        memo[eachWord]=sub_child_list

        if sub_child_list:
            res.append(eachWord)
    
    memo[word]=res
    return res

def find_reducible(wordlist):
    
    res=[]

    for word in wordlist:
        output=is_reducible(word, wordlist)

        if output!=[]:
            res.append(word)

    return res

def find_longest(t1):
    t2=[]

    for word in t1:
        t2.append((len(word), word))

    t2.sort()

    return t2[-1][1]

wordlist=make_word_list()

output=find_reducible(wordlist)

#print find_longest(output)