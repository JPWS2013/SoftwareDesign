"""Module that provides is_palindrome.

Author of is_palindrome: Justin Poh
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
    """Checks if a word is a palindrome or not

    More information about what this function does:

    word: Takes a word that must be a string

    returns True if the word is a Palindrome and returns False if it is not """

    if word==word[::-1]:
        return True

    else:
        return False

print is_palindrome('haneh')
print is_palindrome('hhhhemehhhh')