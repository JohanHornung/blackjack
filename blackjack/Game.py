import Deck

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
        # for conditonal treatement later on
        self.split = False 
        self.double = False
    
    # method which lets the player double his game
    def double(self): # bet arg optional
        pass
    
    # methods which splits his deck
    def split(self, player_hand:list): # bet arg optional
        self.split = True
        """
        Even if the condition should always be true, an error handling
        procedure has been done anyways.
        """
        # make sure that the player has 2 cards (only 2!) and that they have the same value
        self.condition = (len(player_hand)) == 2 and (player_hand[0]["value"] == player_hand[1]["value"])
        if not self.condition:
            if len(player_hand) != 2:
                raise ValueError("Joeur a besoin de 2 cartes!") 
            else:
                raise ValueError("Joueur n'a pas les meme valeurs") 

        self.bets = [self.bet // 2, self.bet // 2]
        self.first_hand = player_hand[0]
        self.second_hand = player_hand[1]
        """
        Basically, the following steps are to play each hand itself, the second
        one gets played if the first one is overbought or when he passed.          
        """

x = Game(50)
x.split([4, 4])