def ridiculous(x):
    total = 0
    for i in 'aeiou':
        y = (ord(i)*(x+1))%17
        d = 12
        for i in range(y):
            d = 83 & y**i
            if i << 6 > 532//(d+5):
                total -= d-x
    return total

def apply_ridiculous(num_list):
    '''
    Purpose: Take in list of integers, then mutate list based on input to ridiculous function
    Input Parameter(s): num_list, a list of integers
    Return Value: Nothing (list will be mutated)
    '''
    for i in range(len(num_list)):
        num_list[i] = ridiculous(num_list[i])
