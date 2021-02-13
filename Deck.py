import random
from config import *
from tools import *

"""
- This folder will contain the Deck class, a deck with 52 distinct cards. The cards/decks
will be tracked over the time of playing as well as those which have been given.
- Deck will contain following methods: 
    - hit(self)
    - split(self)
    - double(self)
    - suiteSize(self)
    - hand of the player (__str__)
- Deck will be initiated with a constructur which takes in the player/dealer hand.
- player_hand / dealer_hand will be an array of sets
- The cards will be a set (dictionnary) 
{   
    "<suit>": {
        "color": red/black,
        "<card>": <value>,
        ...
    }
    ...
}
- Value of the ace has to be set dynamicly
"""

class Deck:
    def __init__(self, player_hand:list, dealer_hand:list):
        # For the player
        self.player_hand = player_hand
        self.player_sum = 0 # first criteria of game break
        # For the dealer
        self.dealer_hand = dealer_hand
        self.dealer_sum = 0 # second criteria of game break
        
        # A new deck is created when the class in initialized 
        self.deck = DECK
        self.suits = SUITS 
        # The cards are a set of sets (of cards)
        self.cards = UNIQUE_CARDS
    
    """
    A method for shuffling the deck is not needed as the card is 
    beeing choosen randomly. In addition, suffling a set is quite
    harder than shuffling an array.
    """
    # def shuffle(self):
    #     pass

    # method which returns a set of the corresponding lengths
    def setLength(self, set):
        self.set = {
                "spades": len(set["spades"]),
                "hearts": len(set["hearts"]),
                "diamonds": len(set["diamonds"]),
                "clubs": len(set["clubs"])
        }
        return self.set

    # method which lets the player hit a card (randomly)
    def hit(self, person):
        # handling the low prob case when the whole deck is empty
        self.refill = (len(self.deck) == 0) or (len(self.cards) == 0) or (len(self.suits) == 0)
        if self.refill: 
            # a simple alternative would be to re-add a new deck
            self.deck = DECK
            # a new picking selection
            self.suits = SUITS
            self.cards = UNIQUE_CARDS  
        
        # unique suit is beeing choosen
        self.suit = random.choice(self.suits)
        # unique card is beeing randomly choosen
        self.card = random.choice(self.cards[self.suit])

        # this specific card is beeing removed from the deck set
        self.card_value = self.deck[self.suit].pop(self.card)

        # this specific card is beeing removed from the cards set
        self.cards[self.suit].remove(self.card)

        
        """
        The following steps are written to spot and delete possible empty sets or decks.
        The corresponding lenghts and attributes are tracked and are part of the
        conditional treatement.
        """
        # tracking the length of the unique cards set
        self.cards_size = self.setLength(self.cards)
        # the whole set will be first removed from the cards set if needed
        self.lengths = self.cards_size.items()
        for suit, length in self.lengths:
            if length == 0:
                self.cards_size.pop(suit)
        
        """
        If theres just the color key left (in the deck set) we delete it as no 
        real cards are there anymore.
        """
        # tracking the set with the number of cards for each suit
        self.suits_size = self.setLength(self.deck)
        
        self.sizes = self.suits_size.items()
        for suit, size in self.sizes:
            if size == 1:
                self.suits.remove(suit) # suit beeing removed from suit list selection
                self.deck.pop(suit) # suit set beeing removed from deck set
        
        """
        The unique card hitted is a set with some
        attributes.     
        """
        self.card_id = {
            "suit": self.suit,
            "color": self.deck[self.suit]["color"],
            "card": self.card,
            "value": self.card_value
        }
        # The chosen card is beeing added to the hand of player/dealer
        if person == "player":
            self.player_hand.append(self.card_id)
        else:
            self.dealer_hand.append(self.card_id)
        
        # return self.card_id, self.deck, self.suits
        
    # method for tracking cards which have been hit/taken
    # def track(self):
    #     pass

    
    def blackjack(self, player): # optional arg
        # if the sum of the cards is 21 the method returns true
        return True if (player[0]["value"] + player[1]["value"] == 21) else False
    
    # method which deals the first for cards out
    def deal(self): # args optional
        for _ in range(2):
            self.hit("dealer")
            self.hit("player")
        
        # check for player blackjack
        self.player_blackjack = self.blackjack(self.player_hand)
        # check for dealer blackjack
        self.dealer_blackjack = self.blackjack(self.dealer_hand)
        # conditional treatement of the bj outcomes will be handled in Game.py
    
    # method which returns the cards (suit + card)
    def cardToString(self):
        self.player_cards = []
        self.dealer_cards = []
        # iteration over both player and dealer hands 
        for cards in self.player_hand:
            self.player_cards.append("a {} {}".format(cards["suit"], cards["card"]))
        for cards in self.dealer_hand:
            self.dealer_cards.append("a {} {}".format(cards["suit"], cards["card"]))
        return self.player_cards, self.dealer_cards
    
    # print method which prints the cards of the player(s)/dealer
    def displayHands(self):
        # if case num_players > 1
            # player_cards will be a 2d array
            # for player in range(num_players):
                # player_cards[player] = [cards["card"] for cards in self.player_hands[player]]
        # for player in range(num_player):
            # print(f"")
        # something like that...
        
        self.player_cards, self.dealer_cards = self.cardToString()
        print(f"The player has: {self.player_cards}")
        print(f"The dealer has: {self.dealer_cards}")





# Deck instance
# game = Deck([], [])
# game.deal()

# debugging
# for i in range(2):
#     game.hit("player")
#     game.hit("dealer")
#     # print(game.cardToString())
#     game.displayHands()
    # print(i)
