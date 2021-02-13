from Game import *
from Deck import *

"""
- This folder will contain the StartingScreen class.
- Methods: choice(self), gameFlow(self), checkout(self)
"""
class StartingScreen:
    def __init__(self):
        self.rounds = 0
        # for gameflow
        self.game = False 
        # for starting the game
        self.bet = 0
    
    # Optional:
    # num_players = int(input("How many players?")) else 1
    
    # to start the menu, we search for a valid input
    def choice(self):
        while True:
            try:
                self.action = int(input(
                """ Welcome to Blackjack (Las Vegas type), please choose an option:\n
                    ||  1 --> Play  ||  2 --> Whitdraw money and quit  || \n
                    Blackjack pays 3:2 ||| Else 2:1\n"""))
            
            except (ValueError):
                print("This isn´t a number")
                continue # until he gets a valid input   
            return self.action

    # method with handles the checkout option for the player
    def checkout(self, bank):
        # check the sign of the bank
        if bank > 0: # if the player gained money
            pass
        else: # if the player lost the money
            pass

    # method which handles the main gameflow of the game
    def gameFlow(self):
        pass
        # if (self.choice == 1):
            # self.game = True
            # Game(self.bet)
            # ..
        # else:
            # self.checkout(bet)



if __name__ == "__main__":
    gameOn = StartingScreen()
    # choice = gameOn.choice()