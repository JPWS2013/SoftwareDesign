def any_lowercase1(s):
	for c in s:
		if c.islower():
			return True

		else:
			return False

def any_lowercase3(s):
	for c in s:
		flag=c.islower()

	return flag

def any_lowercase4(s):
	flag=False
	for c in s:
		print 'c=', c
		print 'flagbefore=', flag
		flag=flag or c.islower()
		print 'flag=', flag
	return flag

def any_lowercase5(s):
	for c in s:
		if not c.islower():
			return False
	return True

print any_lowercase5('tesT')