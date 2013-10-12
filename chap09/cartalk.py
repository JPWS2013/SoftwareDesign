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

def odo_palindrome(raw_reading):
    
    cleanReading=str(raw_reading)
    cleanReading='0'*(6-len(cleanReading))+cleanReading
    lastFour=cleanReading[-4:]

    if lastFour==lastFour[::-1]:

        raw_reading+=1
        cleanReading2=str(raw_reading)
        cleanReading2='0'*(6-len(cleanReading2))+cleanReading2

        lastFive=cleanReading2[-5:]

        if lastFive==lastFive[::-1]:

            raw_reading+=1

            cleanReading3=str(raw_reading)
            cleanReading3='0'*(6-len(cleanReading2))+cleanReading3

            if cleanReading3==cleanReading3[::-1]:
                return True

    return False
    

#print double_letters('brrtt')

test_odo_data=range(999999)

for eachData in test_odo_data:
    if odo_palindrome(eachData)==True:
        clean=str(eachData)
        clean='0'*(6-len(clean))+clean
        print clean

#print odo_palindrome(99)