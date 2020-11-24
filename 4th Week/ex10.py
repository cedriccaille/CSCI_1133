def deposit(bank,client,amount):
    '''
    Purpose: To deposit a specified amount of money into a bank account
    Input Parameter(s): Bank - dictionaru where keys are string of names of clients, and values are integers with amount of money client stored in cents
                        Client - string represents name of clients
                        amount - integer represents amount of money in cents that client needs to deposit
    Return Value: updated dictionary with new values added
    '''
    if client not in bank:
        bank[client] = amount
    else:
        bank[client] = bank[client] + amount
    return bank
