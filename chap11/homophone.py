from pronounce import read_dictionary

def fiveletterfilter(wordDict):
    fiveletterwords=dict()

    for eachWord in wordDict:
        if len(eachWord)==5:
            fiveletterwords[eachWord]=wordDict[eachWord]

        if len(eachWord)==8:
            if eachWord[6]=='(':
                fiveletterwords[eachWord]=wordDict[eachWord]

    return fiveletterwords

def is_homophone_solution(wordDict, word):

    subcase1=word[1:]

    if subcase1 in wordDict:
        if wordDict[subcase1]==wordDict[word]:
            subcase2=word[0]+word[2:]

            if subcase2 in wordDict:

                if wordDict[subcase2]==wordDict[word]:
                    return word + ' ' + subcase1 + ' ' + subcase2

    return False

def test_dictionary(wordDict):

    cleanTestCases=fiveletterfilter(dictPronounce)


    for eachWord in cleanTestCases:
        result=is_homophone_solution(wordDict, eachWord)

        if result != False:
            print result

dictPronounce=read_dictionary()

test_dictionary(dictPronounce)