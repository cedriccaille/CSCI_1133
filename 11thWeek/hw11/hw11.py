#Problem A -- Recursive Collatz
def collatz(n):
    '''
    Purpose:
    Input Parameter(s):
    Return Value:
    '''
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return [n] + collatz(n//2)
    else:
        return [n] + collatz(3*n + 1)

#Problem B -- Checking for Decoys
def is_decoy(lines):
    '''
    Purpose:
    Input Parameter(s):
    Return Value:
    '''
    decoys = ['A','C','M','E']
    if len(lines) < 1:
        return False
    elif lines[0][0] in decoys:
        return True
    elif len(lines) == 1:
        return False
    else:
        return is_decoy(lines[1:])

#Problem C -- Searching all Files
import os

def get_targets(path):
    '''
    Purpose:
    Input Parameter(s):
    Return Value:
    '''
    outlist = []
    for file in os.listdir(path):
        if os.path.isfile(path+'/'+file):
            fp = open(path+'/'+file)
            lst = []
            for lines in fp.readlines():
                lst.append(lines)
            if is_decoy(lst) == False:
                outlist.append(path+'/'+file)
        else:
            get_targets(path+'/'+file)  #Go into a subdirectory
    print(outlist)
    return outlist
