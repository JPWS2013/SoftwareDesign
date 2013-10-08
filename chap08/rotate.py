def rotate_word(s, order):
	"""
	Takes a string and a rotation number and rotates the string by the given amount

	More information about this function:

	s: Needs to be a string
	order: Needs to be an integer

	Returns the rotated string

	"""
	
	newString=''

	for eachChar in s:

		if eachChar.isupper():
			start_code=ord('A')
		elif eachChar.islower():
			start_code=ord('a')
		else:
			newString=newString+eachChar
			continue
		
		total_letters = 26

		startIndex = ord(eachChar)
		endIndex = ((startIndex - start_code + order) % total_letters) + start_code
		newString = newString + chr(endIndex)

	return newString

print rotate_word('V unq ab vqrn gung EBG13 jnf bevtvanyyl hfrq va HFRARG tebhcf gb boshfpngr fcbvyref naq bssrafvir pbagrag. V nyjnlf gubhtug EBG13 jnf whfg n wbxr', 13)