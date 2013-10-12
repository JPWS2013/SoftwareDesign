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
    lastFour=raw_reading[-4:]

    if lastFour==lastFour[::-1]:
        
        lastDigit=raw_reading[-1]
        numLastDigit=int(lastDigit)
        numLastDigit += 1
        raw_reading2=raw_reading[:-1]+str(numLastDigit)
        #print raw_reading2

        lastFive=raw_reading[-5:]

        if lastFive==lastFive[::-1]:

            lastDigit=raw_reading2[-1]
            numLastDigit=int(lastDigit)
            numLastDigit += 1
            raw_reading3=raw_reading2[:-1]+str(numLastDigit)
            
           # print raw_reading3

            if raw_reading3==raw_reading3[::-1]:
                return True

    return False
    

#print double_letters('brrtt')

# test_odo_data=range(999999)

# for i in range (len(test_odo_data)):
#   strungData=str(test_odo_data[i])

#   if len(strungData)==1:
#       correctedstring='00000'+strungData
#       test_odo_data[i]=correctedstring

#   if len(strungData)==2:
#       correctedstring='0000'+strungData
#       test_odo_data[i]=correctedstring

#   if len(strungData)==3:
#       correctedstring='000'+strungData
#       test_odo_data[i]=correctedstring

#   if len(strungData)==4:
#       correctedstring='00'+strungData
#       test_odo_data[i]=correctedstring

#   if len(strungData)==5:
#       correctedstring='0'+strungData
#       test_odo_data[i]=correctedstring

#   if len(strungData)==6:
#       correctedstring=strungData
#       test_odo_data[i]=correctedstring

# for eachData in test_odo_data:
#   if odo_palindrome(eachData)==True:
#       print eachData

print odo_palindrome('200000')