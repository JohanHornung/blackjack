from Deck import *
# from StartingScreen import *
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
        self.game = True
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
    def specialOutcome(self, outcome:str, person:str):
        self.string = ""
        # if the player has a blackjack
        if (person.lower() == "player") and (outcome.lower() == "blackjack"):
            self.blackjack_sum = round(((3 * self.bet) / 2), 2) # a bj pays 3:2
            self.string = f"Congratulations ! You have won {self.blackjack_sum}$ with a Blackjack!"
        # if dealer ouverbought himself
        elif (person.lower() == "player") and (outcome.lower() == "overbought"):
            self.string = f"Congratulations ! You have won {self.bet}$ as the dealer has overbought!"
        # if the dealer has blackjack
        elif (person.lower() == "dealer") and (outcome.lower() == "blackjack"):
            self.string = f"Too bad ! You have lost {self.bet}$, the dealer has Blackjack!"
        # if the player overboughts
        else:
            self.string = f"You overbought ! You lost {self.bet}$"
        
        return self.string
    
    # method which takes the question and all the possibles answers as parameters
    def choosenInput(self, question, *answers) -> bool:
        print(question)
        self.answer = str(input())
        return True if (self.answer.lower() == answers) else False
    
    # method which handles the game itself
    def play(self, player_hand=[], dealer_hand=[]): # bet param already defined 
        while self.game:
            # we first remove the bet from the player from the bank
            self.bank -= self.bet
            # a new game is initialised with a new deck if it is the first
            self.game = Deck(player_hand, dealer_hand)
            self.game.deal() # deal the cards
            self.game.displayHands() # we show both hands
            
            # Check for BJ for both
            if (self.game.player_blackjack):
                self.cause = "blackjack" # for later on statistics
                self.player = "player" # for later on statistics
                self.outcome =  self.specialOutcome(self.cause, self.player)
                # at this point, the game is over
                self.game = False
                break
            
            elif self.game.dealer_blackjack: 
                self.cause = "blackjack" # for later on statistics
                self.player = "dealer" # for later on statistics
                self.outcome =  self.specialOutcome(self.cause, self.player)
                # at this point, the game is over
                self.game = False
                break
            
            # we check if the player has the possibility to split
            self.split_condition = (len(player_hand) == 2) and (player_hand[0]["value"] == player_hand[1]["value"])
            if (self.split_condition): # the player can split and gets asked to
                self.question = "Do you want to split?"
                self.answers = ["yes", "y", "yessir", "of course", "please"]
                self.choice = self.choosenInput(self.question, *self.answers)
                print(self.choice)
            break
                # # if the player wants to split
                # if (self.choice):
                #     self.splitted_hand == True
                #     self.left_split = self.right_split = True # (optional)
                #     # recursive call with the left card as a new deck and the right one
                #     # while (self.left_split):
                #     #     self.play()
                # else:
                #     # we go on
                #     # self.choice = self.choosenInput()
                #     # if (self.choice == <option>):
                #         # hit or stand or double
                #         # check the outcomes (overbought)
                    
                #     # if the player stands (for the second time)
                #     # compare the values and evaluate
                #     # calculate the the bank/budget
                #     # return the new bet or bank/budget
                #     pass
                # # Do you want to play again?
                # # self.restart = StartingScreen()
                # # yes --> self.choice = 1  --> restart.gameFlow()
                # # no --> self.restart.checkout(self.bank)


new_game = Game(2000, 4000)
new_game.play()
# x.game.displaySums()
# print(x.specialOutcome("blackjack", "dealer"))
# x = Deck([], [])
# x.deal()
# x.displayHands()
# x.displaySums()

# x.displayHands()
# winner = x.sumCompare()
# print(winner)