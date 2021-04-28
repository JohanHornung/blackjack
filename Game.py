import numpy as np # for advanced ds (arrays, matrices, ...)
import pandas as pd # data management tools 
import random
import matplotlib.pyplot as plt # mathematical tool
import seaborn as sbn # data visualisation


class Game:
    def __init__(self):
        self.card_types = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10 ,10, 10, 10] # queens, kings and jacks all have a value of 10


    ### HELPER METHODS ###
    
    # make a deck
    def make_decks(self, num_decks, card_types):
        self.new_deck = []
        for _ in range(num_decks):
            for _ in range(4): # 2 for the player and dealer
                self.new_deck.extend(card_types) # adding the card types (['A', 2, 3, 4, ...])
        random.shuffle(self.new_deck)
        return self.new_deck
    
    # the following 2 methods handle the dynamic values of the ace 

    """
    this function lists out all permutations of ace values in the array sum_array
    example: for 2 aces --> [[1, 11], [11, 1], [1, 1], [11, 11]]
    3 unique sums: [2, 12, 22]
    of these 3, only 2 are <=21 so we return [2, 12]
    """
    def get_ace_values(self, temp_list):
        self.sum_array = np.zeros((2**len(temp_list), len(temp_list))) # returns a given array filled with 0´s
        
        # loop for finding all permutations
        for i in range(len(temp_list)):
            n = len(temp_list) - i
            self.half_len = int(2**n * 0.5)
            for rep in range(int(self.sum_array.shape[0] // self.half_len // 2)):
                self.sum_array[rep * 2**n : rep * 2**n + self.half_len, i] = 1
                self.sum_array[rep * 2**n + self.half_len : rep * 2**n + self.half_len * 2, i] = 11
        # only return unique values that are valid (sum <= 21)
        return list(set([int(elem) for elem in np.sum(self.sum_array, axis=1) if elem <= 21]))

    # converts num_aces (int) to a list of lists
    # for example if num_aces=2, the output should be [[1,11],[1,11]]
    def ace_values(self, num_aces):
        temp_list = []
        for i in range(num_aces):
            temp_list.append([1,11]) # as the ace can have the value of 1 or 11
        return self.get_ace_values(temp_list)


    # print(ace_values(5))

    # Total up value of hand
    def total_up(self, hand):
        self.aces = 0
        self.total = 0
        
        for card in hand:
            if card != 'A':
                self.total += card # the card is the int value itself
            else:
                self.aces += 1 # for now 
        
        # call the function ace_values to produce list of possible values for aces in hand
        ace_value_list = self.ace_values(self.aces)
        final_totals = [i + self.total for i in ace_value_list if i + self.total<=21]
        
        if final_totals == []: # if the total sum is higher than 21
            return min(ace_value_list) + self.total
        else:
            return max(final_totals)




# model_df = pd.DataFrame()
# model_df['dealer_card'] = self.dealer_card_feature
# model_df['player_total_initial'] = [total_up(i[0][0:2]) for i in self.player_card_feature]
# model_df['Y'] = [i[0] for i in player_results]

# lose = []
# for i in model_df['Y']:
#     if i == -1:
#         lose.append(1)
#     else:
#         lose.append(0)
# model_df['lose'] = lose

# has_ace = []
# for i in self.player_card_feature:
#     if ('A' in i[0][0:2]):
#         has_ace.append(1)
#     else:
#         has_ace.append(0)
# model_df['has_ace'] = has_ace

# dealer_card_num = []
# for i in model_df['dealer_card']:
#     if i=='A':
#         dealer_card_num.append(11)
#     else:
#         dealer_card_num.append(i)
# model_df['dealer_card_num'] = dealer_card_num





# sum(pd.DataFrame(player_results)[0].value_counts())





# pd.DataFrame(player_results)[0].value_counts()





# data = 1 - (model_df.groupby(by='dealer_card').sum()['lose'] /            model_df.groupby(by='dealer_card').count()['lose'])

# fig, ax = plt.subplots(figsize=(10,6))
# ax = sbn.barplot(x=data.index, 
#                  y=data.values)
# ax.set_xlabel("Dealer's Card",fontsize=16)
# ax.set_ylabel("Probability of Tie or Win",fontsize=16)

# plt.tight_layout()
# plt.savefig(fname='dealer_card_probs', dpi=150)





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







