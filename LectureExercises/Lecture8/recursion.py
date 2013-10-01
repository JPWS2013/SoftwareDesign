def recurse(n, result=0):
    """ My not so good way to do it"""
    
    if type(n)!= int or n<0:
        return 'You did not provide an integer or the number you provided is less than zero which is invalid'
    if n==0:
        return result

    return recurse(n-1, (n+result))

def sum_series(n):

    """ The technically proper way to implement this"""

    if n==0:
        return 0
    
    x=sum_series(n-1)

    return x+n

print recurse(4)