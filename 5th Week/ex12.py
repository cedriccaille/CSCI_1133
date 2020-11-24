def largest():
    '''
    Purpose: Find the maximum value of the inputs and return
    Input Parameter(s): None
    Return: Maximum value
    '''
    max = 0
    num = 1
    while num != 0:
        num = int(input("Enter a number: "))
        if num > max:
            max = num
    return max
