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
    def __init__(self, bet):
        self.bet = bet
        # a new game is initialised with a new deck
        self.player_hand = []
        self.dealer_hand = []
        self.game = Deck(self.player_hand, self.dealer_hand)
        # for conditonal treatement later on
        self.splitted_hand = False 
        self.doubled = False
    
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
        
        # return self.winner # defining the variable in enough

    # method which handles the game itselfj
    def play(self, bet, player_hand, dealer_hand): 
        # self.deal() --> creates bj booleans 
        # Check for BJ for both
        # self.choice()
        # ...
        pass





# x = Game(50)
# x.compare()