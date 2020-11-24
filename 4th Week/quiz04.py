#Problem A
def sound(weight):
    '''
    Purpose: take in single positive integer, weight, and return what the dog's bark would sound like (String)
    Input Parameter(s): weight - positive integer value in pounds
    Return Value: sound of the bark, string type
    '''
    if weight < 13:
        bark = "Yip"
    elif 30 >= weight >= 13:
        bark = "Ruff"
    elif 70 >= weight >= 31:
        bark = "Bark"
    else:
        bark = "Boof"
    return bark

#Problem B
def dollar_sign(pairs, target):
    '''
    Purpose: take in two parameters, pairs is a dictionary and target is a key, and add a "$" to the front of the value where key is in the dictionary
    Input Parameter(s): Pairs -- dictionary; Target -- key
    Return Value: altered dictionary, pairs, that has all the original values with a "$" added to each of them
    '''
    pairs[target] = ("$" + str(pairs[target]))
    return pairs

#Problem C
def grad_TAs(number, labs, students):
    '''
    Purpose: to take the course number, the number of labs sections of that course, and the total students, then divide amount of TAs per section
    Input Parameter(s): number - course number, String; labs - lab sections of the course, integer; students - number of students in the course, integer
    Return Value: number of Graduate TAs assigned to the course, integer
    '''
    if number[0] == "1":
        grads = 1
    elif number[0] == "2":
        grads = labs // 2
    else:
        if students < 50 and labs >= 1:
            grads = 1
        else:
            grads = students // 50
    return grads
