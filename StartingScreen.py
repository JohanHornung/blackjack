from math import *
from Deck import Deck
from Game import Game

"""
- This folder will contain the StartingScreen class.
- Methods: choice(self), gameFlow(self), checkout(self)
"""
class StartingScreen:
    def __init__(self):
        self.rounds = 0
        # for gameflow
        self.game_flow = False
        self.quit = False 
        self.restart = False
        # for starting the game
        self.bet = None

        
    # Optional:
    # num_players = int(input("How many players?")) else 1

    # method which asks the player for another round
    def rematch(self):
        self.action = Game.choosenInput(self, "Do you want to play again?\n")
        if (self.action in ["yes", "y", "of course"]):
            self.restart = True
            self.gameFlow()
        else:
            self.checkout(self.game.bank)
    
    # method with handles the checkout option for the player
    def checkout(self, bank) -> None:
        # for gameflow purposes
        self.game_flow = False
        self.quit = True
        # check the sign of the bank
        if bank > 0: # if the player gained money
            print(f"Congratulations ! You left with {bank}$ the table.")
        else: # if the player lost money
            print(f"Oops ! Looks like you lost {abs(bank - self.bet)}$ on this table.")
            # abs(bank - self.bet) could be wrong (ISSUE #16)
    
    # to start the menu, we search for a valid input
    def welcome(self) -> None:
        while True:
            try:
                self.action = int(input(
                """ Welcome to Blackjack (Las Vegas type), please choose an option:\n
                    ||  1 --> Play  ||  2 --> Whitdraw money and quit  || \n
                    Blackjack pays 3:2 ||| Else 2:1\n"""))
                
            except (ValueError):
                print("This isn´t a number\n")
                continue # until he gets a valid input   
            break
        
        if (self.action == 1) or (self.restart): 
            if not (self.restart): # first game on
                self.bank = int(input("Your budget please\n"))
                # game instance is created
                self.game = Game(self.bank)
            
            # asking once for bet
            self.bet = int(input("Your bets please\n"))
            
            while True:
                # if the players bet is nothing
                if (self.bet != 0):
                    break
                print("You can´t bet with 0$")
                self.bet = int(input("Your bets please\n"))
            
            # we play the game with a valid bet
            self.game.play(self.bet)
        
        else:
            self.checkout(self.game.bank)
        


# function which will launch the blackjack game/program
def main():
    x = StartingScreen()
    x.welcome()
    # x.gameFlow()
    # x.rematch()
    pass




if __name__ == "__main__":
    main()