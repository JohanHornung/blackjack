import numpy as np # for advanced ds (arrays, matrices, ...)
import pandas as pd # data management tools 
import matplotlib.pyplot as plt # mathematical tool
import seaborn as sbn # data visualisation
from Game import * # Game class for the blackjack
import random
import json


class Simulation:
    def __init__(self, stacks, type="smart", num_players=1, num_decks=1):
        self.type = type
        self.stacks = stacks # number of stacks of 1 or more cards
        self.players = num_players
        self.num_decks = num_decks
        self.dealer_card_result = []
        self.player_card_result = []
        self.player_results = []
        self.games_played = 0
        self.game = Game() # 20000 staks, 1 player, 1 deck

    # method which plays the simulated games 1 by 1
    def create(self):
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
                            # simulating both types 
                            if (self.type == "smart"): # smart simulation
                                while ((self.game.total_up(self.players_hands[player]) <= 11) and  
                                    (self.game.total_up(self.players_hands[player]) != 21)):
                                    self.players_hands[player].append(self.cards.pop(0))
                                    
                                    # check for bust again
                                    if self.game.total_up(self.players_hands[player]) > 21:
                                        curr_player_results[0,player] = -1 # loss
                                        break # game over for this player
                            elif (self.type == "random"): # random simulation
                                while ((random.random() >= 0.5) and # 'coin flip' method  
                                    (self.game.total_up(self.players_hands[player]) != 21)):
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
                self.games_played += 1
    
        # print("\nTotal games played: " + str(self.games_played))    
        # print(self.player_results)
    
    # method which evaluates the results of the simulated games
    def evaluate(self): 
        self.wins = self.loses = self.ties = 0
        for result in self.player_results:
            if int(result[0]) == 1: # if the player has won
                self.wins += 1
            elif int(result[0]) == -1: # if the player has lost
                self.loses += 1
            else:
                self.ties += 1
        # print(self.wins, self.loses, self.ties)
        self.stats = {
            "type": self.type,
            "games_played": self.games_played,
            "wins": [self.wins, str((round(self.wins / self.games_played * 100, 2))) + " %"], # [<number>, <percentage>]s
            "loses": [self.loses, str((round(self.loses / self.games_played * 100, 2))) + " %"],
            "ties": [self.ties, str((round(self.ties / self.games_played * 100, 2))) + " %"],
        }
        # print(self.stats)

    def modelisation(self):
        # defining our data model attributes for modelisationisation
        
        # dataframe object (table)
        self.df_model = pd.DataFrame()
        # entry with all the dealer cards
        self.df_model["dealer_card"] = self.dealer_card_result
        # entry with all total sums of the player for each game
        self.df_model["player_total_sums"] = [self.game.total_up(sum[0][0:2]) for sum in self.player_card_result]
        # results of each game (1, 0 or -1)
        self.df_model["results"] = [result[0] for result in self.player_results]

        # print(self.df_model["dealer_card"])
        # print(self.df_model["player_total_sums"])
        # print(self.df_model["results"])

        self.lost = [] # either lost or won (a tie is evaluated as a win)  
        for result in self.df_model['results']:
            if result == -1: # dealer win
                self.lost.append(1)
            else:
                self.lost.append(0)
        # adding the results to a new df attribute
        self.df_model['lost'] = self.lost
        
        # making an array to know if the player had an ace or not
        self.player_has_ace = []
        for card in self.player_card_result:
            # if there is an ace in the tuple of the players cards
            if ("A" in card[0][0:2]): 
                self.player_has_ace.append(1) # == true
            else:
                self.player_has_ace.append(0) # == false
        
        # adding the results to a new df attribute
        self.df_model['player_has_ace'] = self.player_has_ace

        # array for replacing the ace by his numerical value
        dealer_card_val = []
        for card in self.df_model['dealer_card']:
            if card == "A":
                dealer_card_val.append(11)
            else:
                dealer_card_val.append(card)

        # adding the results to a new df attribute
        self.df_model['dealer_card_val'] = dealer_card_val
        
        return self.df_model
    
    # method which returns a table of the player probability of having an ace or not
    def has_ace(self):
        self.aces = (self.df_model.groupby(by ='player_has_ace').sum()['lost'] / 
                    self.df_model.groupby(by='player_has_ace').count()['lost'])
        return self.aces
    
    """
    Method which creates a barplot with the probability of winning (or tie) for all the 
    dealers first cards.
    NOTE: the player always decides based on the FIRST dealer card
    """
    def first_dealer_card_impact(self, xlabel: str, ylabel: str, save_to="images"):
        # print(pd.DataFrame(self.player_results)[0].value_counts())
        # grouping data
        self.data = round(1 - (self.df_model.groupby(by='dealer_card').sum()['lost'] /           
        self.df_model.groupby(by='dealer_card').count()['lost']), 3)
        # print(self.data.index)
        # plotting axes for x and y
        _, ax = plt.subplots(figsize=(10, 6))
        ax = sbn.barplot(x=self.data.index, # [2, 3, 4, ...] 
                        y=self.data.values) 
        # naming labels
        ax.set_xlabel(xlabel, fontsize=15)
        ax.set_ylabel(ylabel, fontsize=15)
        plt.tight_layout()
        # saving
        plt.savefig(fname=f'{save_to}/{self.type}_dealer_card_impact', dpi=200)

    """
    Method which creates a barplot with the probability of winning (or tie) for all the 
    total players hand values.
    """
    def player_value_impact(self, x_label: str, y_label: str, save_to="images"):
        # pretty much the same procedure is done as for the dealers cards
        self.data = 1 - (self.df_model.groupby(by='player_total_sums').sum()['lost'] /
                    self.df_model.groupby(by='player_total_sums').count()['lost'])
        # print(self.data)  
        _, self.axis = plt.subplots(figsize=(10, 6),)
        # obviously the prob of a win or tie is 1 so we ignore it
        self.axis = sbn.barplot(x=self.data[:-1].index,
                         y=self.data[:-1].values)
        self.axis.set_xlabel(x_label, fontsize=15)
        self.axis.set_ylabel(y_label, fontsize=15)

        plt.tight_layout()
        plt.savefig(fname=f'{save_to}/{self.type}_player_value_impact', dpi=200)
        # print(pd.DataFrame(player_results)[0].value_counts())

    # method which saves a heatmap of the probabilities of the player/dealer cards
    def heatmap(self, x_label: str, y_label: str, save_to="images"):
        # creating table without the rows were the player´s sum is above 21
        self.pivot_data = self.df_model[self.df_model['player_total_sums'] != 21]
        # creating a table with all the collected losses for a specific dealer first card value (for each player sum)
        self.losses_pivot = pd.pivot_table(self.pivot_data, values='lost', 
                                      index=['dealer_card_val'], # row
                                      columns = ['player_total_sums'],
                                      aggfunc = np.sum)
        # creating a table with all the collected losses for a specific dealer first card value (for each player card)
        self.games_pivot =  pd.pivot_table(self.pivot_data, values='lost', 
                                      index=['dealer_card_val'],
                                      columns = ['player_total_sums'],
                                      aggfunc = 'count')
        # print(self.games_pivot)
        # collect probabilities of these results
        self.heat_data = 1 - self.losses_pivot.sort_index(ascending=False) / self.games_pivot.sort_index(ascending=False)
        # create plot
        _, self.axis = plt.subplots(figsize=(16, 8))
        # creazte heatmap
        sbn.heatmap(self.heat_data, square=False, cmap="GnBu") # cmap for color palette
        # define axis´s
        self.axis.set_xlabel(x_label, fontsize=16)
        self.axis.set_ylabel(y_label, fontsize=16)

        plt.savefig(fname=f'{save_to}/{self.type}_heat_map', dpi=200)

    # method which returns a barmap comparing 2 types of data frame game results
    def model_comparison(self, other_df, save_to="images"):
        # helper func
        def setup(df_model: object, column: str, xLabel: str):
            pass
        
        # for the player hand values
        # collecting prob. results for both df´s
        self.first_data = 1 - (self.df_model.groupby(by='player_total_sums').sum()['lost'] /                  
                                self.df_model.groupby(by='player_total_sums').count()['lost'])
        self.second_data = 1 - (other_df.groupby(by='player_total_sums').sum()['lost'] /                   
                                other_df.groupby(by='player_total_sums').count()['lost'])
        # creating new dataframe with both new data
        self.data = pd.DataFrame()
        self.data[f"{self.df_model}"] = self.first_data[:-1] # ignore 21 probabilities
        self.data[f"{other_df}"] = self.second_data[:-1] # ignore 21 probabilities
        # create plot
        _, self.axix = plt.subplots(figsize=(12,6))
        # creating both bars for each value with labels
        self.axix.bar(x=self.data.index-0.2, height=self.data[f"{self.df_model}"].values, color='blue', width=0.4, label='smart')
        self.axix.bar(x=self.data.index+0.2, height=self.data[f"{other_df}"].values, color='red', width=0.4, label='random')
        # set labels
        self.axix.set_xlabel("Player's Hand Value", fontsize=16)
        self.axix.set_ylabel("Probability of Tie or Win", fontsize=16)
        # np.arange(4, 20, 1.0), more performant
        plt.xticks([i for i in range(4, 22)]) # sets the steps between each bar
        plt.legend()
        plt.tight_layout()
        plt.savefig(fname=f'{save_to}/{self.type}_player_hand_comparison', dpi=200)
        
        # for the dealers first card 
        # collecting prob. results for both df´s
        self.first_data = 1 - (self.df_model.groupby(by='dealer_card_val').sum()['lost'] /                  
                                self.df_model.groupby(by='dealer_card_val').count()['lost'])
        self.second_data = 1 - (other_df.groupby(by='dealer_card_val').sum()['lost'] /                   
                                other_df.groupby(by='dealer_card_val').count()['lost'])
        # creating new dataframe 
        self.data = pd.DataFrame()
        # 
        self.data[f"{self.df_model}"] = self.first_data
        self.data[f"{other_df}"] = self.second_data
        # create plot
        _, self.axix = plt.subplots(figsize=(12,6))
        # creating both bars for each value with labels
        self.axix.bar(x=self.data.index-0.2, height=self.data[f"{self.df_model}"].values, color='blue', width=0.4, label='smart')
        self.axix.bar(x=self.data.index+0.2, height=self.data[f"{other_df}"].values, color='red', width=0.4, label='random')
        # set labels
        self.axix.set_xlabel("Dealers first card", fontsize=16)
        self.axix.set_ylabel("Probability of Tie or Win", fontsize=16)
        # np.arange(2, 11, 1.0)
        plt.xticks([i for i in range(2, 12)]) # sets the steps between each bar
        plt.legend()
        plt.tight_layout()
        plt.savefig(fname=f'{save_to}/{self.type}_dealer_card_comparison', dpi=200)

    # method which exports main information about the simulations
    def export_headers(self):
        with open(f"JSON/{self.type}_headers.json", "w", encoding="utf-8") as headers:
            json.dump(self.stats, headers, indent=2)
