#Problem A -- Population Growth
def tribble_growth(init_pop,days):
    '''
    Purpose: Takes in initial population and period of time and calculates the increase in population over the period
    Input Parameter(s): init_pop - initial population of tribbles, int; days - scope of time, int
    Return Value: List, increments values at each index by the population growth factor
    '''
    poplist = []
    popgrowth = 1.1
    poplist.append(init_pop)
    i = 0
    while i < days:
        poplist.append(int(poplist[i] * popgrowth))
        i += 1
    return poplist

#Problem B -- Vampire Control
def vampire_growth(initial_vampires, nightly_kill):
    '''
    Purpose: Calculate the changes in a vampire population over a time period
             based on initial population and number of vampires destroyed each night
    Initial Parameter(s): initial_vampires -- Starting vampire population, int
                          nightly_kill -- number of vampires killed each night, int
    Return Value:
    '''
    vamplist = []
    vamplist.append(initial_vampires)
    vampgrowth = 1.5
    i = initial_vampires
    day = 0
    while 0 < i <= 100:
        vamplist.append(int((vamplist[day] * vampgrowth) - nightly_kill))
        day += 1
        i = vamplist[day]
        if vamplist[day] < 0:
            vamplist[day] = 0
    return vamplist

#Problem C -- Rock-Paper-Scissors Round
def rps_round(comp_move):
    '''
    Purpose: Simulates a single round of rock, paper, scissors, where the user plays against the computer
    Input Parameter(s): comp_move, a string, which either contains 'R', 'P', or 'S', for Rock, Paper, or Scissors, respectively
    Return Value: A list containing the player's move, then the result of the match, whether 'W' - a win for player, 'L' - a loss for player, or 'T' a tie.
    '''
    resultlist = []
    valid = ['R', 'P', 'S']
    userchoice = input("Enter R, P, or S: ")
    while userchoice not in valid:
        print("Invalid Input")
        userchoice = input("Enter R, P, or S: ")
    while userchoice in valid:
        resultlist.append(userchoice)
        print("Computer selects " + comp_move)
        if comp_move == 'R' and userchoice == 'S':
            print("Computer wins!")
            resultlist.append('L')
            return resultlist
        elif comp_move == 'R' and userchoice == 'R':
            print("Tie!")
            resultlist.append('T')
            return resultlist
        elif comp_move == 'R' and userchoice == 'P':
            print("Player Wins!")
            resultlist.append('W')
            return resultlist
        elif comp_move == 'S' and userchoice == 'S':
            print("Tie!")
            resultlist.append('T')
            return resultlist
        elif comp_move == 'S' and userchoice == 'R':
            print("Player Wins!")
            resultlist.append('W')
            return resultlist
        elif comp_move == 'S' and userchoice == 'P':
            print("Computer Wins!")
            resultlist.append('L')
            return resultlist
        elif comp_move == 'P' and userchoice == 'S':
            print("Player Wins!")
            resultlist.append('W')
            return resultlist
        elif comp_move == 'P' and userchoice == 'R':
            print("Computer Wins!")
            resultlist.append('L')
            return resultlist
        elif comp_move == 'P' and userchoice == 'P':
            print("Tie!")
            resultlist.append('T')
            return resultlist

#Problem D -- Rock-Paper-Scissors Game
def rps_game(num_rounds):
    '''
    Purpose: Takes number of rounds to play, calls rock, paper, scissors game, and calculate the amount of wins, losses, and ties.
    Input Parameter(s): num_rounds, an integer representing the number of rounds that the game will be played
    Return Value: Dictionary of total wins, losses, and ties
    '''
    resultdict = {'W':0,'L':0,'T':0}
    reslist = []
    i = 0
    while i < num_rounds:
        if i == 0:
            reslist = rps_round('R')
        else:
            reslist = rps_round(reslist[0])
        resultdict[reslist[1]] += 1
        i += 1
    return resultdict
