#Problem A -- Loop Conversion
def mystery(foo,bar,baz):
    '''
    Purpose: Not sure. Change for loops into while loops
    Input Parameter(s): foo,bar,baz. integers?
    Return Value: total sum of all values
    '''
    total = [0,0,0]
    i = 0
    j = foo
    k = foo
    while i < foo:
        total[0] += i
        i += 1
    while j < bar:
        total[1] += j
        j += 1
    while k < bar:
        total[2] += k
        k += baz
    return total

#Problem B -- Divisible by 11 but not 3
def div11not3(start,stop):
    '''
    Purpose: take in two integers, return list of all integers divisible by 11 but not 3 in the range start:stop
    Input Parameter(s): Start, Stop. Both integers, define the range of integers
    Return Value: List of integers divisible by 11 and 3 within the defined range
    '''
    divlist = []
    i = start
    while i <= stop:
        if i % 11 == 0 and i % 3 != 0:
            divlist.append(i)
        i += 1
    return divlist

#Problem C -- Movie Review
def review(movie):
    '''
    Purpose: Take in string movie, ask user to rate movie on scale of 1-4 stars
    Input Parameter(s): Movie -- string. Input -- how many stars for a rating
    Return Value: Final selection as a string
    '''
    rating = ''
    valid = ['1','2','3','4']
    rating = input("How many stars would you give " + movie + "? ")
    while rating not in valid:
        print("Invalid input, please enter 1, 2, 3, or 4.")
        rating = input("How many stars would you give " + movie + "? ")
    return(rating)
