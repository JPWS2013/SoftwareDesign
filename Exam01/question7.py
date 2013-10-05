from unum.units import *

def lift_force(velocity,angle):
	CL=3

	F=0.5*CL*(1.2*kg*(m**-3))*((velocity*m/s)**2)*(0.1*m*m)

	F_corrected=F.asUnit(N)
	
	return F_corrected

print lift_force(3,20)