#Problem A -- Academic Departments
class Department:
    def __init__(self, subject, head, num_profs):
        self.subject = subject
        self.head = head
        self.num_profs = num_profs
    def get_subject(self):
        return self.subject
    def set_subject(self, subject):
        self.subject = subject
    def __add__(self, other):
        combined = Department(str(self.subject) + '&' + str(other.subject), self.head, int(self.num_profs) + int(other.num_profs))
        return combined

#Problem B -- Playing Cards
class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return str(self.value) + ' of ' + str(self.suit)
    def __lt__(self, other):
        values = {'Ace':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5,
          'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10,
          'Jack':11, 'Queen':12, 'King':13}
        if values[self.value] < values[other.value]:
            return True
        else:
            return False

def smallest_card(card_lst):
    return sorted(card_lst)[0]
