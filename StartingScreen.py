from math import *
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
        self.quit = False 
        # for starting the game
        self.bet = 0
        self.bank = 0 # or budget
    
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
        # for gameflow purposes
        self.game = False
        self.quit = True
        # check the sign of the bank
        if bank > 0: # if the player gained money
            print(f"Congratulations ! You left with {bank}$ the table.")
        else: # if the player lost money
            print(f"Oops ! Looks like you lost {abs(bank - self.bet)}$ on this table.")
            # abs(bank - self.bet) could be wrong (ISSUE #16)
    
    # method which handles the main gameflow of the game
    def gameFlow(self, bet):
        pass
        # if (self.choice == 1):
            # self.game = True
            # self.bet = int(input(Your bets please))
            # Game(bet, bank)
            # ..
        # else:
            # self.checkout(self.bank)


# function which will launch the blackjack game/program
def main():
    pass





if __name__ == "__main__":
    main()