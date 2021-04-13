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
    def __init__(self, bank=None):
        # a new game is initialised with a new deck if it is the first
        self.game = Deck([], [])
        
        self.bet = 0
        self.bank = bank # or budget
        
        # for conditonal treatement later on
        self.game_flow = True
        self.splitted_hand = False 
        self.doubled = False
        # for card tracking
        self.stat_cards = []

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
        """
        Even if the condition should always be true, an error handling
        procedure has been done anyways.
        """
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

    # method whicht treats all the special outcomes of the game (blackjack or bust)
    def specialOutcome(self, outcome:str, winner:str):
        self.string = ""
        # if the player has a blackjack
        if (winner.lower() == "player") and (outcome.lower() == "blackjack"):
            self.blackjack_sum = round(((3 * self.bet) / 2), 2) # a bj pays 3:2
            self.string = f"Congratulations ! You have won {self.blackjack_sum}$ with a Blackjack!"
        # if dealer ouverbought himself
        elif (winner.lower() == "player") and (outcome.lower() == "bust"):
            self.string = f"You bust ! You lost {self.bet}$"
        # if the dealer has blackjack
        elif (winner.lower() == "dealer") and (outcome.lower() == "blackjack"):
            self.string = f"Too bad ! You have lost {self.bet}$, the dealer has Blackjack!"
        # if the player busts
        else:
            self.string = f"Congratulations ! You have won {self.bet}$ as the dealer has bust!"
            
        return self.string
    
    # method which takes the question and all the possibles answers as parameters
    def choosenInput(self, question):
        print(question)
        self.answer = str(input())
        return self.answer.lower()
    
    # method which stores results of a game in an dictionnary
    def writeResults(self, winner, nature, game_counter, target=[]):
        self.winner = winner
        self.nature = nature
        self.num_drawn_cards = len(self.game.tracked_cards)

        self.result = {
            "game": game_counter,
            "winner": self.winner, 
            "type": self.nature, 
            "player_sum": self.game.player_sum, 
            "dealer_sum": self.game.dealer_sum, 
            "player_blackjack": self.game.player_blackjack,
            "dealer_blackjack": self.game.dealer_blackjack,
            "number_of_drawn_cards": self.num_drawn_cards,
        }
        target.append(self.result)
    
    # method which draws automatically cards up to n points and returns an array of the results
    def autoDraw(self, n=1, double=False, value=None, tracked_cards=[]):
        # new data entry is created which will be returned
        self.results = []
        self.game_counter = 0 # for data
        for _ in range(n): # for n games played
            self.game = Deck([], []) # new game w/ new deck
            self.game.deal() # first cards are dealed to the player/dealer
            self.game_flow = True
            # self.tracked_cards = []
            self.game_counter += 1
            print(self.game_counter)
            # the type of auto draw is deciding for further instructions
            if double:
                # the player doubles automatically each time
                while self.game_flow:
                    if (self.game.player_blackjack or self.game.dealer_blackjack):
                        # determine the winner
                        if not (self.game.player_blackjack and self.game.dealer_blackjack):
                            self.winner = "player" if self.game.player_blackjack else "dealer"
                        else:
                            self.winner = "draw"
                        # defining the content of the results entry and saving the results in the results array
                        self.writeResults(self.winner, "blackjack", self.game_counter, self.results)
                        break
                    
                    # the player always doubles his cards
                    self.doubleDown()
                    # check for player exceed
                    if (self.game.player_sum > 21):
                            self.writeResults("dealer", "bust", self.game_counter, self.results)
                            self.game_flow = False
                            break
                    # the dealer hits until he has 17 or more
                    while (self.game.dealer_sum < 17 and self.game_flow):
                        self.game.hit("dealer") 
                    
                        if (self.game.dealer_sum == 16):
                            self.game.hit("dealer")
                        
                        # check for exceed
                        elif (self.game.dealer_sum > 21):
                            self.writeResults("player", "bust", self.game_counter, self.results)
                            self.game_flow = False
                            
                    if not self.game_flow:
                        break
                    
                    # default value comparison if nothing happened yet
                    self.winner = self.sumCompare()
                    self.writeResults(self.winner, "comparison", self.game_counter, self.results)        

                # add the tracked cards to the result dictionnary
                self.result["drawn_cards"] = self.game.tracked_cards
                # tracking cards for data manipulation
                # tracked_cards.append(self.game.tracked_cards)
                # self.tracked_cards.append(self.game.card_id)

            else:
                while self.game_flow:
                    if (self.game.player_blackjack or self.game.dealer_blackjack):
                        # determine the winner
                        if not (self.game.player_blackjack and self.game.dealer_blackjack):
                            self.winner = "player" if self.game.player_blackjack else "dealer"
                        else:
                            self.winner = "draw"
                        # defining the content of the results entry and saving the results in the results array
                        self.writeResults(self.winner, "blackjack", self.game_counter, self.results)
                        break   
                    
                    # a new card is beeing drawn up to n points
                    while (self.game.player_sum <= value):
                        self.game.hit("player")
                            
                        if (self.game.player_sum > 21):
                            self.writeResults("dealer", "bust", self.game_counter, self.results)
                            self.game_flow = False
                            break
                    # checking if the game can still go on
                    if not self.game_flow:
                        break
                    
                    # the dealer hits until he has 17 or more
                    while (self.game.dealer_sum < 17):
                        self.game.hit("dealer") 
                    
                        if (self.game.dealer_sum == 16):
                            self.game.hit("dealer")
                        
                        # check for exceed
                        elif (self.game.dealer_sum > 21):
                            self.writeResults("player", "bust", self.game_counter, self.results)
                            self.game_flow = False
                            break
                    
                    # checking if the game can still go on
                    if not self.game_flow:
                        break
                    
                    # default value comparison if nothing happened yet
                    self.winner = self.sumCompare()
                    self.writeResults(self.winner, "comparison", self.game_counter, self.results)        
                    # tracking cards for data manipulation
                    # self.tracked_cards.append(self.game.card_id)
                    break
                
                # drawn cards are added manually
                self.result["drawn_cards"] = self.game.tracked_cards
            
            for card in self.game.tracked_cards:
                self.stat_cards.append(card)
        
        return self.results

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
            
            # distributing the cards
            if (self.splitted_hand):
                self.game.hit("player")
            else:
                self.game.deal() # deal the cards
            
            if (self.game.dealer_blackjack or self.game.player_blackjack):
                self.game.first_deal = False
            self.game.displayHands() # we show both hands
            print("\n")
            self.game.displaySums() # sums are shown
            self.game.first_deal = False
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
            # print(self.game.player_hand)
            ### SPLIT ### 
            
            # self.split_condition = True # debugging 
            self.split_condition = (len(player_hand) == 2) and (player_hand[0]["value"] == player_hand[1]["value"])
            # lets assume for now that you can just split once
            if (self.split_condition) and not (self.splitted_hand): 
                self.question = "Do you want to split?"
                self.choice = self.choosenInput(self.question)
                # if the player wants to split
                if (self.choice in self.positive_answers):
                    self.splitted_hand = True
                    self.left_split = self.right_split = True 
                    self.split(self.game.player_hand)
                    # recursive call to play the game with the left hand
                    if (self.left_split):
                        self.left_split = False
                        self.play(self.game.first_bet, self.game.first_hand, dealer_hand)
                    
                    elif (self.right_split):
                        self.right_split = False
                        self.play(self.game.second_bet, self.game.second_hand, dealer_hand)
            
            ### DOUBLE ###
            
            self.double_choice = input("Do you want to double down?")
            if (self.double_choice in self.positive_answers) or (self.double_choice in self.optional_answers[2]):
                print("the player doubled\n")
                # self.game.first_deal = False
                # we double down the hand
                self.doubleDown()
                self.game.displayHands()
                print("\n")
                self.game.displaySums()
                # if the players cards exceed 21
                if (self.game.player_sum > 21):
                    self.game_flow = False # break out of the loop anyway
                    self.outcome = self.specialOutcome("bust", "player")
                    print(self.outcome) # message for bust
                    self.game_flow = False # break out of the loop anyway
                    break # the game is over          
                else:
                    while (self.game.dealer_sum < 17):
                        self.game.hit("dealer") # draw
                        self.game.displayHands()
                        print("\n")
                        self.game.displaySums()
                        
                        if (self.game.dealer_sum == 16):
                            self.game.hit("dealer")
                        
                        # check for exceed
                        elif (self.game.dealer_sum > 21):
                            self.outcome = self.specialOutcome("bust", "dealer")
                            print(self.outcome) # message for dealer bust
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
                print("\n")
                self.game.displaySums()
                # check if player exceeds 21
                if (self.game.player_sum > 21):
                    self.outcome = self.specialOutcome("bust", "player")
                    print(self.outcome) # message for bust
                    self.game_flow = False # break out of the loop anyway
                    break # the game is over  
                
                self.answer = self.choosenInput("Do you want to hit or stand?")
            
            # check if the player hasn´t bust 
            if not self.game_flow: 
                break
            # dealer must stand on 17 and must draw to 16
            # self.game.first_deal = False
            while (self.game.dealer_sum < 17):
                self.game.hit("dealer") # draw
                self.game.displayHands()
                print("\n")
                self.game.displaySums()

                if (self.game.dealer_sum == 16):
                    self.game.hit("dealer")
                    break
                
                # check for exceed
                elif (self.game.dealer_sum > 21):
                    self.outcome = self.specialOutcome("bust", "dealer")
                    print(self.outcome) # message for dealer bust
                    self.game_flow = False # break out of the loop anyway
                    break # the game is over  
            

            # if the dealer has bust the game ends
            if not self.game_flow: 
                break
            
            # self.game.displayHands()
            # self.game.displaySums()
            
            ### VALUE SHOWDOWN ###
            
            self.winner = self.sumCompare() # determine who the winner is
            self.casualOutcome(self.winner) # print() the outcome and regulate the won sum
            self.game_flow = False # optional
            break
                    
        
        ### REMATCH (in StartingScreen class)###
        # self.restart = StartingScreen()
        # self.restart.rematch()





# new_game = Game(4000)
# new_game.play(50)
# print(new_game.autoDraw(16, 500))
# x.game.displaySums()
# print(x.specialOutcome("blackjack", "dealer"))
# x = Deck([], [])
# x.deal()
# x.displayHands()
# x.displaySums()

# x.displayHands()
# winner = x.sumCompare()
# print(winner)