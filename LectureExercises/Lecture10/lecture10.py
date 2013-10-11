def letnum_check(s):

	"""
	Takes a string and checks if it consists of a single letter followed by a single number

	More information about what this function does:

	s: Must be a string

	Returns boolean True and False values

	"""

	if type(s)!=str:
		print 'You have not provided a string'
		return False

	first_char=ord(s[0].lower())

	if (first_char<=122 and first_char>=97):
		sec_char=ord(s[1])
		if sec_char<=57 and sec_char>=49 :
			return True

	return False

# def letters_numbers(s):
	
# 	if type(s)!=str:
# 		print 'You have not provided a string'
# 		return False

# 	first_char=ord(s[0].lower())
# 	sec_char=ord(s[1].lower())

# 	if first_char==sec_char:
# 		if (first_char>122 and first_char<97):
# 			return False
# 		else:
# 			for i in range(2,len(s)):
# 				while (ord(i.lower())<=122 and ord(i.lower()))>=97):
# 					continue
# 				ord(i)<=57 and ord(i)>=49
# 			else:



# 	else:
# 		if (first_char>122 and first_char<97):
# 			return False
			

# 	return False

def interleave(s1, s2):
	newstring=''

	if len(s1)>len(s2):
		run_range=len(s2)
	else:
		run_range=len(s1)

	for i in range(run_range):
		newstring=newstring+s1[i]+s2[i]

	if len(s1)>len(s2):
		remaining=s1[run_range :]
		newstring=newstring+remaining
		return newstring

	else:
		remaining=s2[run_range :]
		newstring=newstring+remaining
		return newstring


#print letnum_check('3g222a')
print interleave('blondeeeeeeeeeee', 'aloe')

