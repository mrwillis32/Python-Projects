


class Player:
    #Define the attributes of the class
    name = "No name provided"
    username = ""
    password = "abcdeg45"
    account = 0

class College(Player):
    player_rank = 5
    player_injuries = 'ACL'
    pin_number = '1234'

class Coach(Player):
    coach_postion = 'Linebackers'
    coach_years = 2
    pin_number = '5678'

    #Define the methods of the class
    def getLoginInfo(self):
        entry_username = input("Enter your login: ")
        entry_password = input("Enter your password: ")
        if (entry_username == self.username and entry_password == self.password):
            print("Welcome back, {}".format(self.name))
        else:
            print("Not authorized, username needed.")

def getLoginInfo(self):
    entry_username = input("Enter you username: ")
    entry_account = input("Enter your account number: ")
    entry_pin = input("Enter your pin: ")
    if (entry_username == self.username and entry_pin == self.pin_number):
        print("Welcome back, {}!".format(entry_username))
    else:
        print("The pin or username is incorrect")
#The following code invokes the methods inside each class for Player and Coach

player = Player()
player.getLoginInfo()

gm = Coach()
gm.getLoginInfo()
    
    
    
    
    
    
    
  