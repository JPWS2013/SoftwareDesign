def recurse(n, result=0):
    if type(n)!= int:
        return 'You did not provide an integer'
    if n==0:
        return result

    return recurse(n-1, (n+result))

print recurse(4)