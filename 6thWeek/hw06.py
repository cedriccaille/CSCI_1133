#Problem A -- Turtle Drawings
def calc_angle(sides):
    '''
    Purpose: Take in number of desired sides of polygon, and return angle needed to draw that polygon in Turtle
    Input Parameter(s): sides - integer indicating number of polygon sides
    Return Value: angle, float, needed to turn the turtle in order to draw the polygon
    '''
    angle = 1.0*(360 / sides)
    return angle

def draw_polygon(tr, n_sides, side_length):
    '''
    Purpose: Take in parameters of the polygon and draws the polygon through the turtle module
    Input Parameter(s): tr -- turtle object, n_sides -- number of sides (int), side_length -- length of each side (int)
    Return Value: nothing. polygon is drawn in the turtle graphics window
    '''
    angle = calc_angle(n_sides)
    for i in range(n_sides):
        tr.forward(side_length)
        tr.right(angle)

#Problem B -- Detecting Wizards
def wizards(grades, life, sleep):
    '''
    Purpose: Take in three aspects of students lives from lists and determine which are the wizards (appear in all three lists)
    Input Parameter(s): Three lists of strings: grades -- students who get good grades; life -- students hwo have a social life; sleep -- students who get enough sleep
    Return Value: list of all students who appear in all three input lists (the wizards)
    '''
    wizlist = []
    for k in range(len(sleep)):
        if sleep[k] in life and sleep[k] in grades:
            wizlist.append(sleep[k])
    return wizlist

#Problem C -- Who needs loops?
def print_5():
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")

def print_15():
    print_5()
    print_5()
    print_5()

def print_97():
    '''
    Purpose: Prints out "Who needs loops?" 97 times in a row, once per line
    Input Parameter(s): None
    Return Value: None
    '''
    print_15()
    print_15()
    print_15()
    print_15()
    print_15()
    print_15()
    print_5()
    print("Who needs loops?")
    print("Who needs loops?")
