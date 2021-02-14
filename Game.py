from Deck import *
from StartingScreen import *
"""
- This file will contain the Game class (prob. most important).
- It will take no argument in the constructor (maybe the bet)
- The class will track the constant win/loss rates & current benifit/loss
- All constants are inherited from Deck.py
- It will roll out the whole game of n players from the bets to 
the outcomes (6 different them).
- methods: play(self, bet, num_players), ... 
- it will return the new budget of the player (later more for data-analysis) 
"""

class Game:
    def __init__(self, bet, bank):
        self.bet = bet
        self.bank = bank # or budget
        # if the player hasn´t enough money the bet has to be reduced (NEW ISSUE)
        # for conditonal treatement later on
        self.splitted_hand = False 
        self.doubled = False
        # for card tracking
        self.tracked_cards = []

    # method which lets the player double his game
    def doubleDown(self): # bet arg optional
        self.doubled = True
        # when a player doubles down his bet is doubled
        self.bet *= 2
        # he just gets one new card
        self.game.hit("player")
        """
        Further steps will be taken on in the play(self) method, from
        the moment the player gets the new card, his hand is compared
        to the dealer´s one.
        """    
    
    # methods which splits his deck
    def split(self, player_hand:list): # bet arg optional
        self.splitted_hand = True
        """
        Even if the condition should always be true, an error handling
        procedure is done anyways.
        """
        # make sure that the player has 2 cards (only 2!) and that they have the same value
        self.condition = (len(player_hand) == 2) and (player_hand[0]["value"] == player_hand[1]["value"])
        if not self.condition: # this won´t really happen if the code works
            if len(player_hand) != 2:
                raise ValueError("Joeur a besoin de 2 cartes!") 
            else:
                raise ValueError("Joueur n'a pas les meme valeurs") 

        # when the player splits his cards, the same bet is applied to the new hand
        self.first_bet = self.second_bet = self.bet
        # splitting the player hands
        self.first_hand = player_hand[0]
        self.second_hand = player_hand[1]
        """
        Since this method just modifies the needed variables, it returns nothing. The 
        following steps will be done in play(self).
        """
    
    # method which compares the players cards value which the dealer´s
    def sumCompare(self): # args are optional
        self.winner = ""
        if (self.game.player_sum >= self.game.dealer_sum):
            if (self.game.player_sum == self.game.dealer_sum):
                self.winner = "draw"
            else:
                self.winner = "player"
        else:
            self.winner = "dealer"
        
        return self.winner # defining the variable can be enough

    # method whicht treats all the special outcomes of the game (blackjack or overbought)
    def specialOutcomes(self, cause, person):
        pass

    # method which takes the input choice of the player and returns it
    def choosenInput(self):
        pass
    
    # method which handles the game itselfj
    def play(self, bet, player_hand=[], dealer_hand=[]): 
        # a new game is initialised with a new deck if it is the first
        self.game = Deck(player_hand, dealer_hand)
        self.game.deal() # deal the cards
        self.game.displayHands()
        
        # Check for BJ for both
        # if (self.player_blackjack)
            # cause = "blackjack"
            # return specialOutcome(self, cause, player)
        # if (self.dealer_blackjack) 
            # cause = "blackjack"
            # return specialOutcome(self, cause, dealer)
        
        # self.split_condition = (len(player_hand) == 2) and (player_hand[0]["value"] == player_hand[1]["value"])
        # if (self.split_condition): # the player can split
            # if self.split == True
                # self.left_valid = self.right_valid = True (optional)
                # recursive call with the left card as a new deck and the right one
                
        # self.choice = self.choosenInput()
        # if (self.choice == <option>):
            # hit or stand or double
            # check the outcomes (overbought)
        
        # if the player stands (for the second time)
        # compare the values and evaluate
        # calculate the the bank/budget
        # return the new bet or bank/budget
        pass





# x = Deck([], [])
# x.deal()
# x.displayHands()
# x.displaySums()

# x.displayHands()
# winner = x.sumCompare()
# print(winner)