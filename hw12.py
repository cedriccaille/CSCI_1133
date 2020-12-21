#Problem A -- Creating characters
import random
class Character:
    '''
    Purpose: Represents the base character template, which specializations build off of.
    Eliminates redundancy for Pretender and Crewperson classes.

    Instance variables: name - name of character; color - color of character;
    hat - type of character hat; status - whether character is alive or a ghost;
    task_list - list of tasks player must perform

    Methods: Constructor - Initializes the instance variables;
    __repr__ - summarizes the instance variables of a specific character;
    get_identity - returns 'Character'
    '''
    def __init__(self,name,color,hat,num_tasks):
        self.name = name
        self.color = color
        self.hat = hat
        self.status = True
        given_tasks = ['Adjust engine output', 'Calibrate distributor', 'Map course',
        'Clear out O2 filter', 'Destroy asteroids', 'Redirect power', 'Empty garbage',
        'Secure wiring', 'Fill engines tanks', 'Inspect laboratory', 'Move shields',
        'Steady steering', 'Initiate reactor', 'Submit personal info', 'Sign in with ID',
        'Enable manifolds', 'Sync data']
        task_list = []
        for i in range(num_tasks):
            idx = random.randint(0, len(given_tasks)-1)
            task_list.append(given_tasks.pop(idx))
        self.task_list = task_list
    def __repr__(self):
        if self.status == True:
            current = 'Alive'
        elif self.status == False:
            current = 'Ghost'
        return self.name + ': ' + self.color + ', wearing a ' + self.hat + ' - Health status: ' + current
    def get_identity(self):
        return 'Character'
#Problem B -- Crewperson and Pretender
class Crewperson(Character):
    '''
    Purpose: Define one of the characters, Crewperson, inherited from the Character Class
    Instance Variables: See Character documentation
    Methods: Constructor -- initialize variables; Get_Identity -- returns the name of the Class (identity of character);
    complete_task -- character completes a task, announces task completed, then shortens task list. If finished, prints that character completed all tasks.
    '''
    def __init__(self,name,color,hat,num_tasks):
        Character.__init__(self,name,color,hat,num_tasks)
    def get_identity(self):
        return 'Crewperson'
    def complete_task(self):
        if len(self.task_list) == 0:
            print(self.name + ' has completed all their tasks.')
        else:
            print(self.name + ' completed the ' + self.task_list[0] + ' task.')
            self.task_list = self.task_list[1:]

class Pretender(Character):
    '''
    Purpose: Define one of the characters, Pretender, inherited from the character Class
    Instance Variables: See Character documentation
    Methods: Constructor -- initialize variables; Get_Identity -- returns the name of the Class (identity of character);
    eliminate -- eliminates a target, which is a Crewmember that is playing the game. Prints which pretender eliminated which crewperson
    '''
    def __init__(self,name,color,hat,num_tasks):
        Character.__init__(self,name,color,hat,num_tasks)
    def get_identity(self):
        return 'Pretender'
    def eliminate(self,target):
        target.status = False
        print(self.name + ' eliminated ' + target.name + '.')

#Problem C -- Creating a Game class
class Game:
    '''
    Purpose: Simulate a game combining all of the elements previously defined.
    Instance Variables: self.player_list -- represents the pool of players that remain in the game after each round
    Methods: Constructor -- initialize variables; check_winner -- calculates winning condition at each round and if they are met. If so, returns the winner, if not, returns '-';
    meeting -- all of the remaining players vote who they think is a pretender. If player accumulates the most votes, they are eliminated;
    play_game -- simulates a round of the game. Combines the methods together.
    '''
    def __init__(self, player_list):
        self.player_list = player_list
    def check_winner(self):
        no_tasks = []
        cp_alive = []
        cp_dead = []
        pt_alive = []
        for ele in self.player_list:
            if ele.get_identity() == 'Crewperson':
                if ele.status == True:
                    cp_alive.append(ele)
                    if len(ele.task_list) == 0:
                        no_tasks.append(ele)
                elif ele.status == False:
                    cp_dead.append(ele)
                    if ele in cp_alive:
                        cp_alive.remove(ele)
                    if len(ele.task_list) == 0:
                        no_tasks.append(ele)
            elif ele.get_identity() == 'Pretender':
                if ele.status == True:
                    pt_alive.append(ele)
                elif ele.status == False:
                    if ele in pt_alive:
                        pt_alive.remove(ele)
        crewpeople = cp_alive + cp_dead
        if (len(no_tasks) == len(crewpeople)) or len(pt_alive) == 0:
            print('Crewpersons win!')
            return 'C'
        elif len(pt_alive) >= len(cp_alive):
            print('Pretenders win!')
            return 'P'
        elif (len(no_tasks) == len(crewpeople) or len(pt_alive) == 0) and (len(pt_alive) >= len(cp_alive)):
            print('Crewpersons win!')
            return 'C'
        else:
            return '-'
        self.player_list = pt_alive + crewpeople
    def meeting(self):
        players = {}
        total = self.player_list
        for ele in total:
            idx = random.randint(1, len(total) - 1)
            if ele.status == True:
                choice = total[idx]
                if ele.name == choice.name:
                    pass
                else:
                    if choice in players.keys():
                        players[choice] += 1
                    else:
                        players[choice] = 1
                    print(ele.name + ' voted for ' + choice.name)
        highest = max(players.values())
        outlist = []
        for voted in players.items():
            if voted[1] == highest:
                outlist.append(voted[0])
        if len(outlist) == 1:
            print(outlist[0].name + ' was eliminated.')
            outlist[0].status = False
            return outlist[0].name
        else:
            print('Nobody was eliminated.')
            return None
    def play_game(self):
        while self.check_winner() != 'C' or self.check_winner() != 'P':
            for player in self.player_list:
                if player.get_identity() == 'Crewperson':
                    tasks = random.randint(1,3)
                    for i in range(tasks):
                        player.complete_task()
                if player.get_identity() == 'Pretender' and player.status == True:
                    idx = random.randint(0,len(self.player_list) - 1)
                    choice = self.player_list[idx]
                    if choice.status == True:
                        if choice.get_identity() == 'Crewperson':
                            player.eliminate(choice)
                    else:
                        pass
            if self.check_winner() == 'C' or self.check_winner() == 'P':
                return self.check_winner()
            elif self.check_winner() == '-':
                self.meeting()
                new_result = self.check_winner()
                if new_result == 'C' or new_result == 'P':
                    return new_result

# p_list = [Pretender("Jerry", "Blue", "mohawk", 4),
#               Crewperson("Jackson", "Orange", "bird nest", 4),
#               Crewperson("Yuchen", "Purple", "witch hat", 4),
#               Crewperson("Zaela", "White", "party hat", 4),
#               Crewperson("Audrey", "Lime", "wet floor sign", 4),
#               Crewperson("Rachel", "Pink", "sticky note", 4),
#               Crewperson("Nikhil", "Cyan", "pirate hat", 4),
#               Pretender("Julia", "Yellow", "green fedora", 4),
#               Crewperson("Greta", "Brown", "lab goggles", 4),
#               Crewperson("Nate", "Red", "banana peel", 4)]
