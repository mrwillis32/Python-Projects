


class Player:
    #Define the attributes of the class
    name = "No name provided"
    username = ""
    password = "abcdeg45"
    account = 0

class College(Player):
    player_rank = 5
    player_injuries = 'ACL'

class Coach(Player):
    coach_postion = 'Linebackers'
    coach_years = 2

    #Define the methods of the class
    def login(self):
        entry_username = input("Enter your login: ")
        entry_password = input("Enter your password: ")
        if (entry_username == self.username and entry_password == self.password):
            print("Welcome back, {}".format(self.name))
        else:
            print("Not authorized, username needed.")
    #New instance for Player class
    new_player = Player()
    #Call the login method using the new object
    new_player.login()




def __init__(self, name, username, password, ssn):
    self.name = name
    self.username = username
    self.password = password
    self.account = account
