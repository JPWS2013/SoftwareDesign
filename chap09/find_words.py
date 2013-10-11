"""Test code for palindrome.py.

Author: Allen B. Downey
"""

def has_no_e(s):
	for eachChar in s:
		if ord(eachChar.lower())==101:
			return False

	return True

def morethantwenty(s):
	if len(s)>20:
		return True
	return False

def avoids(s,avoid):

	for eachChar in s:
		for eachAvoid in avoid:
			if eachChar.lower()==eachAvoid.lower():
				return False

	return True

def use_only(s, use):
	for eachChar in s:
		for eachUse in use:
			if eachChar.lower() != eachUse.lower():
				return False

	return True

def uses_all(s, useall):

	for eachUseAll in useall:

		doesExist=False	
			
		for eachChar in s:
			if eachChar.lower()==eachUseAll.lower():
				doesExist=True
		
		if doesExist==False:
			return False

	return True

def is_abecedarian(s):

	for i in range(1, len(s)):

		currentChar=ord(s[i-1].lower())
		nextChar=ord(s[i].lower())

		if currentChar>nextChar:
			return False
	return True

def main():
    for line in open('words.txt'):

        # remove whitespace from the beginning and end
        word = line.strip()

        #if morethantwenty(word):
        	#print word

        #only print palindromes
        #if has_no_e(word):
            #print word

        #if avoids(word, 'aeiou'):
        	#print word

        #if use_only(word, 'zing'):
        	#print word

        #if uses_all(word, 'aeiouy'):
        	#print word

        if is_abecedarian(word):
        	print word



if __name__ == '__main__':
    main()
