def first(s):
	return s[0]

def rest(s):
	return s[1:]

def check_a(s):
	if len(s)==0:
		return True

	if first(s) != 'a':
		return False
	
	return check_b(rest(s))

def check_b(s):
	if len(s)==0:
		return True

	if first(s) != 'b':
		return False

	return check_a(rest(s))

print check_a('aba')