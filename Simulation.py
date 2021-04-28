import numpy as np # for advanced ds (arrays, matrices, ...)
import pandas as pd # data management tools 
import random
import matplotlib.pyplot as plt # mathematical tool
import seaborn as sbn # data visualisation
from Game import * # Game class for the blackjack

class Simulation:
    def __init__(self, stacks, num_players=1, num_decks=1):
        self.stacks = stacks # number of stacks of 1 or more cards
        self.players = num_players
        self.num_decks = num_decks
        self.dealer_card_result = []
        self.player_card_result = []
        self.player_results = []
        self.game = Game() # 20000 staks, 1 player, 1 deck

    # method which plays the simulated games 1 by 1
    def simulation(self):
        for _ in range(self.stacks): # iteration through the stacks
            
            self.blackjack = set(['A',10]) # {10, "A"} --> all possible blackjacks
            self.cards = self.game.make_decks(self.num_decks, self.game.card_types)
            
            while (len(self.cards) > 15): # the stack is switched when they are 15 cards left
                # the curr_player_results array will track the outcome of the simulated games 
                # (1 for a win, 0 for a tie and -1 for a loss)
                curr_player_results = np.zeros((1, self.players)) 
                # the dealers hand
                self.dealer_hand = []
                # each list is a player´s hand
                self.players_hands = [[] for player in range(self.players)]

                # deal the first card to player and dealer
                for player, _ in enumerate(self.players_hands): 
                    self.players_hands[player].append(self.cards.pop(0)) # first in last out
                
                self.dealer_hand.append(self.cards.pop(0))
                
                # deal the second card to player and dealer
                for player, _ in enumerate(self.players_hands): 
                    self.players_hands[player].append(self.cards.pop(0))
                
                self.dealer_hand.append(self.cards.pop(0))

                # dealer checks for 21
                if set(self.dealer_hand) == self.blackjack: # if the dealer has a blackjack
                    
                    for player in range(self.players):
                        # if the player does not have a blackjack he loses
                        if set(self.players_hands[player]) != self.blackjack: 
                            curr_player_results[0, player] = -1 # the corresponding players 0 is replaced by -1
                        else: # tie
                            curr_player_results[0, player] = 0 # tie
                else:
                    for player in range(self.players): # for each player
                        
                        # players check for 21
                        if set(self.players_hands[player]) == self.blackjack:
                            curr_player_results[0, player] = 1 # win
                        
                        else:
                            """
                            Now, the player has the choice to either hit or stay, if we suppose that
                            the probability for hitting is the same as for staying, we can at each turn 
                            generate a random value between 0 and 1, if this value is higher than 0.5, 
                            the player hits, else we stay (do nothing). We additionally check for busts.
                            """
                            while (random.random() >= 0.5) and \
                                (self.game.total_up(self.players_hands[player]) != 21):
                                self.players_hands[player].append(self.cards.pop(0))
                                
                                # check for bust again
                                if self.game.total_up(self.players_hands[player]) > 21:
                                    curr_player_results[0,player] = -1 # loss
                                    break # game over for this player
                
                # dealer hits until 17 or more
                while self.game.total_up(self.dealer_hand) < 17:    
                    self.dealer_hand.append(self.cards.pop(0))
                
                # compare dealer hand to self.players hand but first check if dealer busted
                if self.game.total_up(self.dealer_hand) > 21:
                    for player in range(self.players): # for each player
                        if curr_player_results[0, player] != -1: # if the player hasn´t already lost
                            curr_player_results[0, player] = 1 # the player wins
                
                else: # nobody busted
                    for player in range(self.players): # for each player 
                        # we compare the values
                        if (self.game.total_up(self.players_hands[player]) > self.game.total_up(self.dealer_hand)):
                            # if the player hasn´t already busted
                            if self.game.total_up(self.players_hands[player]) <= 21: 
                                curr_player_results[0, player] = 1 # win
                        
                        elif self.game.total_up(self.players_hands[player]) == self.game.total_up(self.dealer_hand):
                            curr_player_results[0, player] = 0 # tie
                        else:
                            curr_player_results[0, player] = -1 # loss
                
                # track results for each game
                self.dealer_card_result.append(self.dealer_hand[0])
                self.player_card_result.append(self.players_hands)
                self.player_results.append(list(curr_player_results[0]))
                # print(self.dealer_card_result, self.player_card_result, self.player_results)

                print("player: " + str(self.game.total_up(self.players_hands[player])),
                     "dealer: " + str(self.game.total_up(self.dealer_hand)),
                     "result: " + str(curr_player_results[0]), # -1 || 0 || 1 
                     "\n" 
                    )    
    
    def evaluate(self):
        pass            




simulation = Simulation(100)
simulation.simulation()