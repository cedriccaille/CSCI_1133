#Problem A
def create_username(first, last):
    '''
    Purpose: To generate a university username from a student's first and last name
    Input Parameter(s): Student first name and last name (both string variables)
    Return Value: generated username for university
    '''
    username = last + first[0]
    return username

#Problem B
def readable(input_list):
    '''
    Purpose: To convert a list (example precipitation data) into a human-readable string
    Input Parameter(s): a list that comes in the format of precipiation amounts
                        (in) from a location within the country (Type: List)
    Return Value: generates an english sentence of the data that is comprehensible (Type: String)
    '''
    convertedlist = str("On " + input_list[6] + " " + str(input_list[7]) + ", " + str(input_list[5])
                    + ", " + input_list[0] + ", " + input_list[1] + " received "
                    + str(input_list[-1]) + " inches of precipitation.")
    return convertedlist

#Problem C
def switch(teams, driver):
    '''
    Purpose: To switch a driver with their partner (swap a dictionary key with its value, making the value the key)
    Input Parameter(s): a dictionary called teams, and a key of that dictionary called driver
    Return Value: takes the input driver of the dictionary teams and makes its associated value become the new driver (key). Returns modified dictionary
    '''
    orig_value = teams[driver]
    del teams[driver]
    teams[orig_value] = driver
    return teams

#Problem D
def winners(finish_order, teams):
    '''
    Purpose: To display the winners of the race taking the value from a dictionary
    Input Parameter(s): a list of the order of race finishers (finish_order) and a dictionary of contestants grouped by team (teams)
    Return Value: prints a string of the winners of the race by using the list order and retrieving the values from the dictionary (Type: String)
    '''
    firstdriver = finish_order[0]
    firstpartner = teams[firstdriver]
    return str(firstdriver + " and " + firstpartner + " won the race!")
