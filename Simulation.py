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
        self.games_played = 0
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
                            while ((random.random() >= 0.5) and (self.game.total_up(self.players_hands[player]) != 21)):
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
                # print(self.dealer_card_result, self.player_card_result, self.player_results)

                # print("player: " + str(self.game.total_up(self.players_hands[player])),
                #      "dealer: " + str(self.game.total_up(self.dealer_hand)),
                #      "result: " + str(curr_player_results[0]), # -1 || 0 || 1 
                #     )    
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
            "games_played": self.games_played,
            "wins": [self.wins, str((round(self.wins / self.games_played * 100, 2))) + " %"], # [<number>, <percentage>]s
            "loses": [self.loses, str((round(self.loses / self.games_played * 100, 2))) + " %"],
            "ties": [self.ties, str((round(self.ties / self.games_played * 100, 2))) + " %"],
        }
        # print(self.stats)

    def modelisation(self):
        # defining our data model attributes for modelisationisation
        
        # dataframe object (table)
        self.model_df = pd.DataFrame()
        # entry with all the dealer cards
        self.model_df["dealer_card"] = self.dealer_card_result
        # entry with all total sums of the player for each game
        self.model_df["player_total_sums"] = [self.game.total_up(sum[0][0:2]) for sum in self.player_card_result]
        # results of each game (1, 0 or -1)
        self.model_df["results"] = [result[0] for result in self.player_results]

        # print(self.model_df["dealer_card"])
        # print(self.model_df["player_total_sums"])
        # print(self.model_df["results"])

        self.lost = [] # either lost or won (a tie is evaluated as a win)  
        for result in self.model_df['results']:
            if result == -1: # dealer win
                self.lost.append(1)
            else:
                self.lost.append(0)
        # adding the results to a new df attribute
        self.model_df['lost'] = self.lost
        
        # making an array to know if the player had an ace or not
        self.player_has_ace = []
        for card in self.player_card_result:
            # if there is an ace in the tuple of the players cards
            if ("A" in card[0][0:2]): 
                self.player_has_ace.append(1) # == true
            else:
                self.player_has_ace.append(0) # == false
        
        # adding the results to a new df attribute
        self.model_df['player_has_ace'] = self.player_has_ace

        # array for replacing the ace by his numerical value
        dealer_card_num = []
        for card in self.model_df['dealer_card']:
            if card == "A":
                dealer_card_num.append(11)
            else:
                dealer_card_num.append(card)

        # adding the results to a new df attribute
        self.model_df['dealer_card_num'] = dealer_card_num




simulation = Simulation(50)
simulation.simulation()
simulation.evaluate()
simulation.modelisation()
print(simulation.model_df)

        # sum(pd.DataFrame(player_results)[0].value_counts())





        # pd.DataFrame(player_results)[0].value_counts()





        # data = 1 - (self.model_df.groupby(by='dealer_card').sum()['lose'] /           
        # self.model_df.groupby(by='dealer_card').count()['lose'])

        # fig, ax = plt.subplots(figsize=(10,6))
        # ax = sbn.barplot(x=data.index, 
        #                  y=data.values)
        # ax.set_xlabel("Dealer's Card",fontsize=16)
        # ax.set_ylabel("Probability of Tie or Win",fontsize=16)

        # plt.tight_layout()
        # plt.savefig(fname='dealer_card_probs', dpi=150)
        # second chart





# data = 1 - (model_df.groupby(by='player_total_initial').sum()['lose'] /            model_df.groupby(by='player_total_initial').count()['lose'])

# fig, ax = plt.subplots(figsize=(10,6))
# ax = sbn.barplot(x=data[:-1].index,
#                  y=data[:-1].values)
# ax.set_xlabel("Player's Hand Value",fontsize=16)
# ax.set_ylabel("Probability of Tie or Win",fontsize=16)

# plt.tight_layout()
# plt.savefig(fname='player_hand_probs', dpi=150)





# model_df.groupby(by='has_ace').sum()['lose'] / model_df.groupby(by='has_ace').count()['lose']





# pivot_data = model_df[model_df['player_total_initial'] != 21]

# losses_pivot = pd.pivot_table(pivot_data, values='lose', 
#                               index=['dealer_card_num'],
#                               columns = ['player_total_initial'],
#                               aggfunc = np.sum)

# games_pivot =  pd.pivot_table(pivot_data, values='lose', 
#                               index=['dealer_card_num'],
#                               columns = ['player_total_initial'],
#                               aggfunc = 'count')

# heat_data = 1 - losses_pivot.sort_index(ascending=False) / games_pivot.sort_index(ascending=False)

# fig, ax = plt.subplots(figsize=(16,8))
# sbn.heatmap(heat_data, square=False, cmap="PiYG");

# ax.set_xlabel("Player's Hand Value",fontsize=16)
# ax.set_ylabel("Dealer's Card",fontsize=16)

# plt.savefig(fname='heat_map_random', dpi=150)





# self.stacks = 50000
# self.players = 1
# self.num_decks = 1

# card_types = ['A',2,3,4,5,6,7,8,9,10,10,10,10]

# self.dealer_card_feature = []
# self.player_card_feature = []
# player_results = []

# for stack in range(self.stacks):
#     blackjack = set(['A',10])
#     dealer_cards = make_decks(self.num_decks, card_types)
#     while len(dealer_cards) > 20:
        
#         curr_player_results = np.zeros((1,self.players))
        
#         dealer_hand = []
#         player_hands = [[] for player in range(self.players)]

#         # Deal FIRST card
#         for player, hand in enumerate(player_hands):
#             player_hands[player].append(dealer_cards.pop(0))
#         dealer_hand.append(dealer_cards.pop(0))
#         # Deal SECOND card
#         for player, hand in enumerate(player_hands):
#             player_hands[player].append(dealer_cards.pop(0))
#         dealer_hand.append(dealer_cards.pop(0))

#         # Dealer checks for 21
#         if set(dealer_hand) == blackjack:
#             for player in range(self.players):
#                 if set(player_hands[player]) != blackjack:
#                     curr_player_results[0,player] = -1
#                 else:
#                     curr_player_results[0,player] = 0
#         else:
#             for player in range(self.players):
#                 # self.players check for 21
#                 if set(player_hands[player]) == blackjack:
#                     curr_player_results[0,player] = 1
#                 else:
#                     # Hit only when we know we will not bust
#                     while total_up(player_hands[player]) <= 11:
#                         player_hands[player].append(dealer_cards.pop(0))
#                         if total_up(player_hands[player]) > 21:
#                             curr_player_results[0,player] = -1
#                             break
        
#         # Dealer hits based on the rules
#         while total_up(dealer_hand) < 17:
#             dealer_hand.append(dealer_cards.pop(0))
#         # Compare dealer hand to self.players hand but first check if dealer busted
#         if total_up(dealer_hand) > 21:
#             for player in range(self.players):
#                 if curr_player_results[0,player] != -1:
#                     curr_player_results[0,player] = 1
#         else:
#             for player in range(self.players):
#                 if total_up(player_hands[player]) > total_up(dealer_hand):
#                     if total_up(player_hands[player]) <= 21:
#                         curr_player_results[0,player] = 1
#                 elif total_up(player_hands[player]) == total_up(dealer_hand):
#                     curr_player_results[0,player] = 0
#                 else:
#                     curr_player_results[0,player] = -1
#         #print('player: ' + str(total_up(player_hands[player])),
#         #      'dealer: ' + str(total_up(dealer_hand)),
#         #      'result: ' + str(curr_player_results)
#         #     )    
        
#         # Track features
#         self.dealer_card_feature.append(dealer_hand[0])
#         self.player_card_feature.append(player_hands)
#         player_results.append(list(curr_player_results[0]))

# model_df_smart = pd.DataFrame()
# model_df_smart['dealer_card'] = self.dealer_card_feature
# model_df_smart['player_total_initial'] = [total_up(i[0][0:2]) for i in self.player_card_feature]
# model_df_smart['Y'] = [i[0] for i in player_results]

# lose = []
# for i in model_df_smart['Y']:
#     if i == -1:
#         lose.append(1)
#     else:
#         lose.append(0)
# model_df_smart['lose'] = lose

# has_ace = []
# for i in self.player_card_feature:
#     if ('A' in i[0][0:2]):
#         has_ace.append(1)
#     else:
#         has_ace.append(0)
# model_df_smart['has_ace'] = has_ace

# dealer_card_num = []
# for i in model_df_smart['dealer_card']:
#     if i=='A':
#         dealer_card_num.append(11)
#     else:
#         dealer_card_num.append(i)
# model_df_smart['dealer_card_num'] = dealer_card_num





# data_smart = 1 - (model_df_smart.groupby(by='dealer_card_num').sum()['lose'] /                  model_df_smart.groupby(by='dealer_card_num').count()['lose'])
# data_random = 1 - (model_df.groupby(by='dealer_card_num').sum()['lose'] /                   model_df.groupby(by='dealer_card_num').count()['lose'])

# data = pd.DataFrame()
# data['smart'] = data_smart
# data['random'] = data_random

# fig, ax = plt.subplots(figsize=(12,6))
# ax.bar(x=data.index-0.2, height=data['smart'].values, color='blue', width=0.4, label='Smart')
# ax.bar(x=data.index+0.2, height=data['random'].values, color='red', width=0.4, label='Coin Flip')
# ax.set_xlabel("Dealer's Card",fontsize=16)
# ax.set_ylabel("Probability of Tie or Win",fontsize=16)
# plt.xticks(np.arange(2, 12, 1.0))

# plt.legend()
# plt.tight_layout()
# plt.savefig(fname='dealer_card_probs_smart', dpi=150)





# data_smart = 1 - (model_df_smart.groupby(by='player_total_initial').sum()['lose'] /                  model_df_smart.groupby(by='player_total_initial').count()['lose'])
# data_random = 1 - (model_df.groupby(by='player_total_initial').sum()['lose'] /                   model_df.groupby(by='player_total_initial').count()['lose'])

# data = pd.DataFrame()
# data['smart'] = data_smart[:-1]
# data['random'] = data_random[:-1]

# fig, ax = plt.subplots(figsize=(12,6))
# ax.bar(x=data.index-0.2, height=data['smart'].values, color='blue', width=0.4, label='Smart')
# ax.bar(x=data.index+0.2, height=data['random'].values, color='red', width=0.4, label='Coin Flip')
# ax.set_xlabel("Player's Hand Value",fontsize=16)
# ax.set_ylabel("Probability of Tie or Win",fontsize=16)
# plt.xticks(np.arange(4, 21, 1.0))

# plt.legend()
# plt.tight_layout()
# plt.savefig(fname='player_hand_probs_smart', dpi=150)



