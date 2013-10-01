import math

def complex_mag(complexnum):
	if type(complexnum)!=complex:
		print "This is not a complex number"

	else:
		return abs(complexnum)


def complex_ang(complexnum):
	if type(complexnum)!=complex:
		print "This is not a complex number"

	else:
		return math.atan2(complexnum.imag, complexnum.real)

def sn_ratio (signal, noise):
	return 10*math.log10(float(signal)/noise)

def binomial(n,k):
	n_fac=math.factorial(n)
	k_fac=math.factorial(k)
	nminusk_fac=math.factorial(n-k)

	return n_fac/(k_fac*nminusk_fac)

def stirling(n):
	lnfac=(math.e)**(n*math.log(n)-n)
	return len(str(lnfac)

alpha=stirling(3)

print alpha
#alpha=complex(3,4)