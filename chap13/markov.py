"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import string
import random
from swampy.Lumpy import Lumpy

lumpy=Lumpy()


def process_file(filename, skip_header=True):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
   
    Returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = file(filename)
    fullwordlist=[]
    # if skip_header:
    #     skip_gutenberg_header(fp)

    for line in fp:
        holder=process_line(line,hist)
        #print holder
        fullwordlist.extend(holder)
    return fullwordlist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break


def process_line(line, hist):
    """Adds the words in the line to the histogram.

    Modifies hist.

    line: string
    hist: histogram (map from word to frequency)
    """
    # replace hyphens with spaces before splitting
    line = line.replace('-', ' ')
    wordlist=[]

    for word in line.split():
        # remove punctuation and convert to lowercase
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()

        wordlist.append(word)
        # update the histogram
        #hist[word] = hist.get(word, 0) + 1
    return wordlist

def most_common(hist):
    """Makes a list of the key-value pairs from a histogram and
    sorts them in descending order by frequency.

    hist: map from word to the number of times it appears

    returns: list of (word, frequency) pairs, sorted by frequency
    """
    t = []
    res=[]

    for word, frequency in hist.items():
        t.append((frequency, word))

    t.sort(reverse=True)

    for frequency, word in t:
        res.append((word, frequency))
    return res


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    
    hist: histogram (map from word to frequency
    num: number of words to print
    """
    t = most_common(hist)
    print 'The most common words are:'
    for freq, word in t[:num]:
        print word, '\t', freq


def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.

    d1, d2: dictionaries

    returns: new dictionary
    """
    res = {}
    
    for key in d1:
        if key not in d2:
            res[key]=None

    return res


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)
  

def random_word(hist):
    """Chooses a random word from a histogram.

    The probability of each word is proportional to its frequency.
    """
    
    t=[]

    for word, freq in hist.items():
        t.extend([word]*freq)

    return random.choice(t)

mark_dict={}

def markov_dic(wordlist):
    for i in range(len(wordlist)-2):
        prefix=(wordlist[i], wordlist[i+1])
        suffix=wordlist[i+2]
        
        if prefix in mark_dict:
            mark_dict[prefix].append(suffix)
        else:
            mark_dict[prefix]=[suffix]

def markov_assembly(wordlist, n=50):
    start_tuple=random.choice(mark_dict.keys())
    res=list(start_tuple)
    allSuffix=mark_dict[start_tuple]
    print res
    print allSuffix

    for i in range(n):
        nextSuffix=random.choice(allSuffix)
        res.append(nextSuffix)
        nextPrefix=(res[-2], res[-1])

        if nextPrefix in mark_dict:
            allSuffix=mark_dict[nextPrefix]
        else:
            nextPrefix=random.choice(mark_dict.keys())
            res.append(nextPrefix[0])
            res.append(nextPrefix[1])
            allSuffix=mark_dict[nextPrefix]

    #lumpy.object_diagram()
    
    return res

def markov_assembly_complicated(wordlist, n=100):
    start_tuple=random.choice(mark_dict.keys())
    res=list(start_tuple)
    allSuffix=mark_dict[start_tuple]

    for i in range(n):
        ready=False
        nextSuffix=random.choice(allSuffix)
        res.append(nextSuffix)
        nextPrefix=(res[-2], res[-1])

        if nextPrefix in mark_dict:
            allSuffix=mark_dict[nextPrefix]
        else:
            for eachKey in mark_dict:
                if nextPrefix[1]==eachKey[1]:
                    print eachKey
                    allSuffix=mark_dict[eachKey]
                    ready=True

            if ready==False:

                nextPrefix=random.choice(mark_dict.keys())
                res.append(nextPrefix[0])
                res.append(nextPrefix[1])
                allSuffix=mark_dict[nextPrefix]
    #lumpy.object_diagram()

    return res

def print_assembly(assemList):
    res=''
    for eachWord in assemList:
        res=res+eachWord+' '

    return res

if __name__ == '__main__':

    words = process_file('muchado.txt', skip_header=False)
    markov_dic(words)

    #markList=markov_assembly(words)
    markList=markov_assembly_complicated(words)
    print print_assembly(markList)