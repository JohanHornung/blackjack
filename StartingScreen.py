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
        self.bet = None
        self.bank = 0 # or budget
    
    # Optional:
    # num_players = int(input("How many players?")) else 1
    
    # to start the menu, we search for a valid input
    def choice(self) -> int:
        while True:
            try:
                self.action = int(input(
                """ Welcome to Blackjack (Las Vegas type), please choose an option:\n
                    ||  1 --> Play  ||  2 --> Whitdraw money and quit  || \n
                    Blackjack pays 3:2 ||| Else 2:1\n"""))
            
            except (ValueError):
                print("This isn´t a number")
                continue # until he gets a valid input   
            if (self.action == 1): # playes for the first time
                self.bank = int(input("Your budget please"))
            
            return self.action

    # method with handles the checkout option for the player
    def checkout(self, bank) -> None:
        # for gameflow purposes
        self.game = False
        self.quit = True
        # check the sign of the bank
        if bank > 0: # if the player gained money
            print(f"Congratulations ! You left with {bank}$ the table.")
        else: # if the player lost money
            print(f"Oops ! Looks like you lost {abs(bank - self.bet)}$ on this table.")
            # abs(bank - self.bet) could be wrong (ISSUE #16)
    
    # method which asks the player for another round
    def rematch(self):
        # self.rematch = gameRematch(self) (needs to be written)
        # yes --> self.choice = 1  --> restart.gameFlow()
        # self.restart = StartingScreen()
        # no --> self.restart.checkout(self.bank)
        pass

    # method which handles the main gameflow of the game
    def gameFlow(self):
        self.action = self.choice() # menu screen
        if (self.action == 1):
            self.bet = int(input("Your bets please"))
            self.game = Game(self.bank)
            self.game.play(self.bet)
        else:
            self.checkout(self.bank)


# function which will launch the blackjack game/program
def main():
    pass





if __name__ == "__main__":
    main()