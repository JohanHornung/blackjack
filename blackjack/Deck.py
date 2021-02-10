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
        self.cards = CARDS
    
    """
    method for shuffling the deck is not needed as the card is 
    beeing choosen randomly.
    """
    # def shuffle(self):
    #     pass

    def suitSize(self):
        self.suits_size = {
                "spades": len(self.deck["spades"]),
                "hearts": len(self.deck["hearts"]),
                "diamonds": len(self.deck["diamonds"]),
                "clubs": len(self.deck["clubs"])
        }
        return self.suits_size

    # method which lets the player hit a card (randomly)
    def hit(self, person):
        # unique card is beeing randomly choosen
        self.suit = random.choice(self.suits)
        self.card = random.choice(self.cards)
        
        """
        The unique card hitted is a set with some
        attributes. It will be removed from the
        deck and added to the hand of the player/dealer.        
        """
        self.card_id = {
            "suit": self.suit,
            "color": self.deck[self.suit]["color"],
            "card": self.card,
            # as the hitted card is automaticly removed we use .pop()
            "value": self.deck[self.suit].pop(self.card)
        }
        
        # tracking the set with the number of cards for each suit
        self.suits_size = self.suitSize()
        """
        If theres just the color key left we delete it as no real 
        cards are there anymore.
        """
        # process of spotting and remvoing the possible empty suit set
        self.items = self.suits_size.items()
        for suit, size in self.items:
            if size == 1:
                self.suits.remove(suit) # suit beeing removed from list selection
                self.deck.pop(str(suit)) # suit set beeing removed from deck set
        
        # The chosen card is beeing added to the hand of player/dealer
        if person == "player":
            self.player_hand.append(self.card_id)
        else:
            self.dealer_hand.append(self.card_id)
        
        return self.card_id, self.deck, self.suits
        
        

    
    # method for tracking cards which have been hit/taken
    # def track(self):
    #     pass
    
    # method which lets the player double a card
    def double(self):
        pass
    
    # methods which splits the cards
    def split(self):
        pass


    # print method which prints the current deck/hand
    def displayHands(self):
        return "Player´s Hand: ",self.player_hand, "Dealer´s Hand: ", self.dealer_hand


game = Deck([], [])
game.hit("player")
