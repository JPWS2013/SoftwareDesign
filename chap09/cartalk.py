def double_letters(s):

    """

    Takes a word as a string and determines if it contains 3 consecutive double double_letters

    s: Must be a string of 6 or more characters

    Returns boolean True and False Values

    """
    if len(s)<6:
        return False

    for i in range(len(s)-5):
        if s[i].lower()==s[i+1].lower():
            if s[i+2].lower()==s[i+3].lower():
                if s[i+4].lower()==s[i+5].lower():
                    return True

    return False

def palindrome_test(reading, start, end):
    """
    Tests if a given odometer reading is a palindrome when sliced between the start and end points given

    reading: Must be an integer or string
    start: must be an integer
    end: must be an integer

    Returns boolean True or False Values


    """
    cleanReading='0'*(6-len(str(reading)))+str(reading) #Assumes any number with a zero in front is also a valid number and adds zeros to the front of the number to make it 6 digits 
    testString=cleanReading[start:end]

    return testString==testString[::-1]


def odo_palindrome(raw_reading):
    
    """
    Tests for the conditions given in the cartalk puzzle

    raw_reading: Must be an integer or string

    Returns boolean True or False Values

    """

    return palindrome_test(raw_reading, 2, 6) and palindrome_test(raw_reading+1, 1, 6) and palindrome_test(raw_reading+2, 1, 5) and palindrome_test(raw_reading+3, 0, 6)
    
def make_word_list():
    """Reads lines from a file and builds a list using append.

    returns: list of strings
    """
    t = []
    
    for line in open('words.txt'):
        word=line.strip()

        t.append(word)

    return t

# words=make_word_list()

# for eachWord in words:
#     if double_letters(eachWord):
#         print eachWord


# test_odo_data=range(999999)

# for eachData in test_odo_data:
#     if odo_palindrome(eachData)==True:
#         clean=str(eachData)
#         clean='0'*(6-len(clean))+clean
#         print clean

#print odo_palindrome(199999)