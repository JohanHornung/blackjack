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
    def __init__(self, bank):
        # a new game is initialised with a new deck if it is the first
        self.game = Deck([], [])
        
        self.bet = 0
        self.bank = bank # or budget
        
        # for conditonal treatement later on
        self.game_flow = True
        self.splitted_hand = False 
        self.doubled = False
        # for card tracking
        self.tracked_cards = []

        # all possibles answers to the questions
        self.positive_answers = ["yes", "y", "yessir", "of course", "yes please"]
        self.negative_answers = ["no", "n", "nosir", "not", "no please"]
        self.optional_answers = [["hit", "h", "hit me"], ["stand", "s"], ["double", "d"]]

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
    
    # methods which splits a deck
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
        self.game.first_bet = self.game.second_bet = self.bet
        # splitting the player hands
        self.game.first_hand = player_hand[0]
        self.game.second_hand = player_hand[1]
        """
        Since this method just modifies the needed variables, it returns nothing. The 
        following steps will be done in play(self).
        """
    
    # method which compares the players cards value which the dealer´s
    def sumCompare(self) -> str: # args are optional
        self.winner = ""
        if (self.game.player_sum >= self.game.dealer_sum):
            if (self.game.player_sum == self.game.dealer_sum):
                self.winner = "draw"
            else:
                self.winner = "player"
        else:
            self.winner = "dealer"
        
        return self.winner # defining the variable can be enough

    # method which treats the casual outcomes of the game (value comparison)
    def casualOutcome(self, winner:str):
        if (winner == "player"):
            self.bet *= 2
            self.bank += self.bet
            print(f"Congratulations! You have more points than the dealer,{self.bet}$ have been added to your bank account.")
        elif (winner == "dealer"):
            print(f"Too bad! You have less points than the dealer, you have lost {self.bet}$ on this game.")
        else: #draw
            print(f"Draw game! You have as many points as the dealer. You get back your bet, {self.bet}$.")

    # method whicht treats all the special outcomes of the game (blackjack or overbought)
    def specialOutcome(self, outcome:str, winner:str):
        self.string = ""
        # if the player has a blackjack
        if (winner.lower() == "player") and (outcome.lower() == "blackjack"):
            self.blackjack_sum = round(((3 * self.bet) / 2), 2) # a bj pays 3:2
            self.string = f"Congratulations ! You have won {self.blackjack_sum}$ with a Blackjack!"
        # if dealer ouverbought himself
        elif (winner.lower() == "player") and (outcome.lower() == "overbought"):
            self.string = f"You overbought ! You lost {self.bet}$"
        # if the dealer has blackjack
        elif (winner.lower() == "dealer") and (outcome.lower() == "blackjack"):
            self.string = f"Too bad ! You have lost {self.bet}$, the dealer has Blackjack!"
        # if the player overboughts
        else:
            self.string = f"Congratulations ! You have won {self.bet}$ as the dealer has overbought!"
            
        return self.string
    
    # method which takes the question and all the possibles answers as parameters
    def choosenInput(self, question) -> str:
        print(question)
        self.answer = str(input())
        return self.answer.lower()
    
    # method which handles the game itself
    def play(self, bet, player_hand=[], dealer_hand=[]): # bet param already defined 
        self.bet = bet
        while self.game_flow:
            # if the player hasn´t enough money the bet has to be reduced (ISSUE#25 fixed)
            if (self.bet > self.bank):
                print(f"You are not able to bet {self.bet}$. You only have {self.bank}$ in your bank.")
                # the bet will be set automatically to the bank budget
                self.bet = self.bank
                self.bank = 0
                print("Your bet has been set to your maximum budget.\n")
            else:
                # we remove the bet from the player from the bank
                self.bank -= self.bet
            
            
            self.game.deal() # deal the cards
            self.game.displayHands() # we show both hands
            self.game.displaySums() # sums are shown

            # Check for BJ for both
            if (self.game.player_blackjack):
                self.cause = "blackjack" # for later on statistics
                self.player = "player" # for later on statistics
                self.outcome =  self.specialOutcome(self.cause, self.player)
                print(self.outcome)
                # at this point, the game is over
                self.game_flow = False # break out of the loop anyway
                break
            
            elif (self.game.dealer_blackjack): 
                self.cause = "blackjack" # for later on statistics
                self.player = "dealer" # for later on statistics
                self.outcome =  self.specialOutcome(self.cause, self.player)
                print(self.outcome)
                # at this point, the game is over
                self.game_flow = False # break out of the loop anyway
                break
            
            ### SPLIT ### (for later)
            
            # self.split_condition = True # debugging 
            # self.split_condition = (len(player_hand) == 2) and (player_hand[0]["value"] == player_hand[1]["value"])
            # # lets assume for now that you can just split once
            # if (self.split_condition) and not (self.splitted_hand): 
            #     self.question = "Do you want to split?"
            #     self.choice = self.choosenInput(self.question)
            #     # if the player wants to split
            #     if (self.choice in self.positive_answers):
            #         self.splitted_hand = True
            #         self.left_split = self.right_split = True 
            #         self.split(self.game.player_hand)
            #         # recursive call with the left card as a new deck and the right one
            #         # while (self.left_split):
            #         #     self.left_split = False
            #             # self.play(self.game.first_bet, self.game.first_hand, self.game.dealer_hand)
            #     else:
            #         # we go on
            #         self.choice = self.choosenInput()
            #         if (self.choice in self.optional_answers[0]): # player chose to hit
            #             self.hit = True # to know when to break out of the loop
            #             while (self.hit):
            #                 self.game.hit("player")
            #                 # display cards & sums
            #                 self.game.displayHands()
            #                 self.game.displaySums()
                        
            #                 # check for overbought
            #                 if (self.game.player_sum > 21):
            #                     self.game_flow = False # break out of the loop anyway
            #                     self.outcome = self.specialOutcome("overbought", "player")
            #                     print(self.outcome) # message for overbought
            #                     # we want to know if the player has splitted his cards
            #                     if (self.left_split):
            #                         self.left_split = False
            #                         print("Let´s switch to your other hand...\n")
            #                         self.play(self.game.second_bet, self.game.second_hand, self.game.dealer_hand)
            #                     else:
            #                         self.game_flow = False # break out of the loop anyway
            #                         break # the game is finished, he can play again
            #             # if the player got at this point (both hands overbought) he lost
            #             break            
            #         # if the player stands 
            #         elif (self.choice in self.optional_answers[1]):
            #             # check if he has splitted
            #             if (self.splitted_hand):
            #                 print("Let´s switch to your other hand...\n")
            #                 self.play(self.game.second_bet, self.game.second_hand, self.game.dealer_hand)
            #             else:
            #                 # value comparison
            #                 pass
            
            ### DOUBLE ###
            
            self.double_choice = input("Do you want to double down?")
            if (self.double_choice in self.positive_answers) or (self.double_choice in self.optional_answers[2]):
                print("the player doubled")
                # we double down the hand
                self.doubleDown()
                self.game.displayHands()
                self.game.displaySums()
                # if the players cards exceed 21
                if (self.game.player_sum > 21):
                    self.game_flow = False # break out of the loop anyway
                    self.outcome = self.specialOutcome("overbought", "player")
                    print(self.outcome) # message for overbought
                    self.game_flow = False # break out of the loop anyway
                    break # the game is over          
                else:
                    while (self.game.dealer_sum < 17):
                        self.game.hit("dealer") # draw
                        self.game.displayHands()
                        self.game.displaySums()
                        if (self.game.dealer_sum == 16):
                            self.game.hit("dealer")
                            break
                        # check for exceed
                        elif (self.game.dealer_sum > 21):
                            self.outcome = self.specialOutcome("overbought", "dealer")
                            print(self.outcome) # message for dealer overbought
                            self.game_flow = False # break out of the loop anyway
                            break # the game is over  1
                    # we compare the sums
                    self.winner = self.sumCompare() # determine who the winner is
                    self.casualOutcome(self.winner) # print() the outcome and regulate the won sum
                    self.game_flow = False # optional
                    break
                    # dealer draws cards until 17

            ### HIT/STAND ###

            self.answer = self.choosenInput("Do you want to hit or stand?")
            
            while (self.answer in self.optional_answers[0]): # hit
                self.game.hit("player")
                self.game.displayHands()
                self.game.displaySums()
                # check if player exceeds 21
                if (self.game.player_sum > 21):
                    self.game_flow = False # break out of the loop anyway
                    self.outcome = self.specialOutcome("overbought", "player")
                    print(self.outcome) # message for overbought
                    self.game_flow = False # break out of the loop anyway
                    break # the game is over  
                
                self.answer = self.choosenInput("Do you want to hit or stand?")
            
            # check if the player hasn´t overbought himself
            if not self.game_flow: 
                break
            
            # dealer must stand on 17 and must draw to 16
            while (self.game.dealer_sum < 17):
                self.game.hit("dealer") # draw
                self.game.displayHands()
                self.game.displaySums()

                if (self.game.dealer_sum == 16):
                    self.game.hit("dealer")
                    break
                # check for exceed
                elif (self.game.dealer_sum > 21):
                    self.outcome = self.specialOutcome("overbought", "dealer")
                    print(self.outcome) # message for dealer overbought
                    self.game_flow = False # break out of the loop anyway
                    break # the game is over  
            

            # if the dealer has overbought himself the game ends
            if not self.game_flow: 
                break
            
            ### VALUE SHOWDOWN ###
            
            self.winner = self.sumCompare() # determine who the winner is
            self.casualOutcome(self.winner) # print() the outcome and regulate the won sum
            self.game_flow = False # optional
            break
                    
        
        ### REMATCH (in StartingScreen class)###
        





new_game = Game(4000)
new_game.play(50)
# x.game.displaySums()
# print(x.specialOutcome("blackjack", "dealer"))
# x = Deck([], [])
# x.deal()
# x.displayHands()
# x.displaySums()

# x.displayHands()
# winner = x.sumCompare()
# print(winner)