def tautonym(s):

	totalLength=len(s)
	eachLength=len(s)/2

	firstPart=s[:eachLength]
	secondPart=s[eachLength:]

	if firstPart==secondPart:
		return True
	else:
		return False

print tautonym('  ')