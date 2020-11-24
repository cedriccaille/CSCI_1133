#Problem A -- Longest String
def longest(str_list):
    '''
    Purpose: Take in list of strings, returns longest string
    Input Parameter(s); str_list, list of strings
    Return Value: longest string value
    '''
    longest = str_list[0]
    for i in range(len(str_list)):
        print(i)
        if len(str_list[i]) > len(longest):
            longest = str_list[i]
    return longest

#Problem B -- Only Primes
def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def only_primes(num_list):
    '''
    Purpose: take in list of positive integers, return new list of elements that are prime numbers
    Input Parameter(s): num_list, list of positive integers
    Return Value: new list of all prime numbers from input list
    '''
    primelist = []
    for i in range(len(num_list)):
        if prime(num_list[i]) == True:
            primelist.append(num_list[i])
    return primelist

#Problem C -- Swapping the Minimum
def swap_min(vals):
    '''
    Purpose: Take in list of integers, swaps minimum value with value at index 0
    Input Parameter(s): vals, list of integers
    Return Value: altered list, where value at index 0 is replaced with the minimum value of the list
    '''
    minimum = vals[0]
    for i in range(len(vals)):
        if vals[i] <= minimum:
            minimum = vals[i]
            idx = i
    vals[0], vals[idx] = vals[idx], vals[0]
    return vals
