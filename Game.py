#!/usr/bin/env python

import numpy as np
import random


class Game:
    def __init__(self):
        self.card_types = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10 ,10, 10, 10] # queens, kings and jacks all have a value of 10
    ### HELPER METHODS ###
    
    # make a deck
    def make_decks(self, num_decks, card_types):
        self.new_deck = []
        for _ in range(num_decks):
            for _ in range(6): # 6 decks per stack
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
            for rep in range(int(self.sum_array.shape[0] // self.half_len // 2)): # math
                self.sum_array[rep * 2**n : rep * 2**n + self.half_len, i] = 1 # math
                self.sum_array[rep * 2**n + self.half_len : rep * 2**n + self.half_len * 2, i] = 11 # math
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
    def total(self, hand):
        self.aces = 0
        self.total_value = 0
        
        for card in hand:
            if card != 'A':
                self.total_value += card # the card is the int value itself
            else:
                self.aces += 1 # for now 
        
        # call the function ace_values to produce list of possible values for aces in hand
        ace_value_list = self.ace_values(self.aces)
        final_totals = [ace + self.total_value for ace in ace_value_list if ace + self.total_value <= 21]
        
        if final_totals == []: # if the total sum is higher than 21
            return min(ace_value_list) + self.total_value
        else:
            return max(final_totals)

