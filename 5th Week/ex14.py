def prime(n):
    '''
    Purpose: take a positive integer n >= 2 and determine whether number is prime
    Input Parameter(s): n, a positive integer >= 2
    Return Value: Boolean for whether number, n, is prime or not
    '''
    i = 2
    while i < n:
        if n % i == 0 and i != n:
            return False
        i+=1
    return True
