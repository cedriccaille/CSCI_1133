def expo(x,y):
    '''
    Purpose: take in two positive integers and return the exponent x^y
    Input Parameter(s): X, Y, positive integers
    Return Value: exponent x^y
    '''
    prod = 1
    i = 0

    while i < y:
        total = 0
        j = 0
        while j < x:
            total += prod
            j += 1
        prod = total
        i += 1
    return prod

print(expo(3,5))