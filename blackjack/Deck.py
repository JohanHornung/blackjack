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
    # constructor with some instance var´s in it
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

    # method which lets the player hit a card (random)
    def hit(self, person):
        # Checking if the len() from one suit set is 0 
        self.condition = True
        self.suits_size = self.suitSize()
        for value in self.suits_size.values():
            if value == 0:
                self.condition = False
        
        if self.condition:
            # unique card is beeing randomly choosen
            self.suit = random.choice(self.suits)
            self.card = random.choice(self.cards)
            
            """
            The unique card hitted is a set with her
            attributes. It will be removed from the
            deck and added to the hand of the player/dealer.        
            """
            self.card_id = {
                "suit": self.suit,
                "color": self.deck[self.suit]["color"],
                "card": self.card,
                # as the hitted card is removed from the deck we use .pop()
                "value": self.deck[self.suit].pop(self.card)
            }
            
            # keeping track of the suits set length
            self.suits_size = self.suitSize()
            """
            If theres just the color left we delete the color as no real 
            cards are there anymore
            """
            self.items = self.suits_size.items()
            for suit, size in self.items:
                if size == 1:
                    self.suits.remove(suit)
                    self.deck[suit].pop("color")
            
            # The chosen card is beeing added to the hand of player/dealer
            if person == "player":
                self.player_hand.append(self.card_id)
            else:
                self.dealer_hand.append(self.card_id)
            
            return self.card_id, self.deck, self.suits
        
        else: # if one of the suits are not there anymore
            pass # only thing which has to be done

    
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
# print(game.player_hand[0])
# print(game.deck)

# print(game.displayHands())