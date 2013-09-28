"""Module that provides is_palindrome.

Author of is_palindrome: you
"""

def first(word):
    """Returns the first character of a word.

    word: string

    returns: length 1 string
    """
    return word[0]


def last(word):
    """Returns the first character of a word.

    word: string

    returns: length 1 string
    """
    return word[-1]


def middle(word):
    """Returns all but the first and last character of a word.

    word: string

    returns: string
    """
    return word[1:-1]


def is_palindrome(word):
    """Write a good Docstring here."""

    if len(word)<2:
        print "The word you have entered is not a valid word to check for a palindrome"
        return False
    
    firstletter=first(word)
    lastletter=last(word)

    if firstletter.lower()==lastletter.lower():
        center=middle(word)

        if len(center)!=0:
            is_palindrome(center)

    else:
        return False
    # TODO: fill in the body of this function
    return True

testword='HAnNah'

test_result=is_palindrome(testword)

if test_result==True:
    print testword, "is a palindrome!"

else:
    print testword, "is not a palindrome!"