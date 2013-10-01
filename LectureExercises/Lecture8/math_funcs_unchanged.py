import math

def complex_mag(c):
    print math.hypot(c.real, c.imag)

def complex_angle(c):
    print math.atan2(c.real, c.imag)

c = complex(3, 4)
complex_mag(c)
complex_angle(c)

def signal_noise(signal, noise):
    print 10 * math.log10(float(signal) / noise)

signal_noise(2, 1)

def binomial_coef(n, k):
    num = math.factorial(n)
    denom = math.factorial(k) * math.factorial(n-k)
    print num / denom

binomial_coef(10, 3)

def factorial_length(n):
    print len(str(math.factorial(n)))

def factorial_length2(n):
    print (n * math.log(n) - n) / math.log(10)

factorial_length(100)
factorial_length2(100)