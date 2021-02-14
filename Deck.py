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
- Value of the ace has to be set dynamically
"""

class Deck:
    def __init__(self, player_hand:list, dealer_hand:list) -> None: # theoretically these parameters are optional
        # class variables for the player
        self.player_hand = player_hand
        self.player_sum = 0 # important criteria of game break
        # class variables for the dealer
        self.dealer_hand = dealer_hand
        self.dealer_sum = 0 # important criteria of game break
        # class variables for card tracking
        self.tracked_cards = []
        self.card_id = None # nothing has been drawn yet (condition for cardTack(self))
        self.person = "" # this will be a new key in the copied card id´s set

        # a new deck is created when the Class in initialized 
        self.deck = DECK
        self.suits = SUITS # all the suits in an array
        # the unique cards are a set of arrays (["Ace", "King", "Queen", ...])
        self.unique_cards = UNIQUE_CARDS
    """
    - The '-> None' means that this function/method returns None
    - A method for shuffling the deck is not needed as an unique card 
    is beeing choosen randomly. In addition, suffling a set is quite
    harder than shuffling an array for example.
    """
    
    # method which returns a set of the suit lengths
    def setLength(self, set) -> dict:
        self.set = {
                "spades": len(set["spades"]), # if set is empty len(set) == 0
                "hearts": len(set["hearts"]),
                "diamonds": len(set["diamonds"]),
                "clubs": len(set["clubs"])
        }
        return self.set

    # method which spots an Ace and replace the card value by 1 if needed
    def isAce(self, card_id, person_sum) -> None:
        if (card_id["card"] == "Ace"): # if the drawned card is an Ace
        # if the current person´s sum would exceed 21 with that ace, the value of the Ace is set to 1
                if (person_sum + card_id["value"] > 21): 
                        card_id["value"] = 1
    
    # method for tracking cards which have been drawned
    def cardTrack(self, tracking_list:list, element=None) -> None:
        # the goal is to append all drawn cards to an array
        if element: # if (at least) a card has been drawn
            tracking_list.append(element)

    # method which lets the player randomly hit a card 
    def hit(self, person:str) -> None:
        # we want to know who is playing
        self.person = person 
        # handling the case when the deck is empty
        self.refill = (len(self.deck) == 0) or (len(self.unique_cards) == 0) or (len(self.suits) == 0) # boolean
        if self.refill: 
            # a simple alternative is to re-add a new deck
            self.deck = DECK
            # and to add a new picking selection
            self.suits = SUITS
            self.unique_cards = UNIQUE_CARDS  
        
        # Process of hitting a card randomly:
        
        # unique suit is beeing choosen
        self.suit = random.choice(self.suits)
        # unique card is beeing randomly choosen
        self.card = random.choice(self.unique_cards[self.suit])

        # this specific card is beeing removed from the deck set
        self.card_value = self.deck[self.suit].pop(self.card)

        # this specific card is beeing removed from the cards set
        self.unique_cards[self.suit].remove(self.card)

        
        """
        The following steps are written to spot and delete possible empty sets or decks.
        The corresponding lenghts and attributes are tracked and are part of the
        conditional treatement.
        """
        # tracking the length of the unique cards set
        self.unique_cards_length = self.setLength(self.unique_cards)
        
        # the whole suit set will be removed from the unique cards set if needed
        self.lengths = self.unique_cards_length.items()
        # we then iterate trough the keys and values of the set
        for suit, length in self.lengths:
            if length == 0: # if one suit set is empty we remove it
                self.unique_cards_length.pop(suit) 
        
        """
        If theres just the color key left (in the deck set) we delete it as no 
        real cards are there anymore.
        """
        # tracking the set with the number of cards left for each suit
        self.suits_size = self.setLength(self.deck)
        
        # same procedure for spotting empty suit sets
        self.sizes = self.suits_size.items()
        for suit, length in self.sizes:
            if length == 1: # when just the color is left
                self.suits.remove(suit) # suit beeing removed from suit list selection
                self.deck.pop(suit) # suit set beeing removed from deck set
        
        """
        The unique drawn card will be a set with important attributes. This set will be
        appended to the person´s hand later on.     
        """
        self.card_id = {
            "suit": self.suit,
            "color": self.deck[self.suit]["color"],
            "card": self.card,
            "value": self.card_value 
        }
        
        # Procces of tracking down the drawned card´s ID

        # first a copy of the card_id is created
        self.tracked_card = self.card_id.copy()
        # we add the "person" key in the copied set as it is important to know who drawed the card
        self.tracked_card["person"] = self.person
        # we add the copied set to the tracked cards
        self.cardTrack(self.tracked_cards, self.tracked_card)
        
        # the chosen card is beeing added to the hand of player/dealer
        if person.lower() == "player":
            # check if the card is an ace
            self.isAce(self.card_id, self.player_sum)
            # card´s id is appended to the player hand
            self.player_hand.append(self.card_id)
            # player´s sum is adjusted
            self.player_sum += self.card_id["value"] # self.card_value does not change dynamically (ace)

        else:
            # same procedure for the dealer
            self.isAce(self.card_id, self.dealer_sum)
            self.dealer_hand.append(self.card_id)
            self.dealer_sum += self.card_id["value"] # self.card_value does not change dynamically (ace)
        
        # as the class var´s are modified, hit(self) doesnt have to return anything
    
    # method returns a boolean which is True when the player has a blackjack
    def blackjack(self, player) -> bool:
        # if the sum of the cards is 21 the method returns true
        return True if (player[0]["value"] + player[1]["value"] == 21) else False
    
    # method which deals the first cards out and checks for BJ
    def deal(self) -> None: # params optional
        for _ in range(2):
            self.hit("dealer")
            self.hit("player")
        
        # check for player blackjack
        self.player_blackjack = self.blackjack(self.player_hand)
        # check for dealer blackjack
        self.dealer_blackjack = self.blackjack(self.dealer_hand)
        # conditional treatement of the bj outcomes will be handled in Game.py
    
    # method which returns the cards (suit + card)
    def cardsToString(self) -> tuple:
        self.player_cards = []
        self.dealer_cards = []
        # iteration over both player and dealer hands 
        for cards in self.player_hand:
            self.player_cards.append("a {} {}".
            format(cards["suit"], cards["card"]))
            # diamond Ace, spades Ten, ...
        
        # when the dealer just has two cards, just the second one is shown (ISSUE #17 (closed))
        if (len(self.dealer_hand) == 2):
            self.dealer_cards.append("an unknown card") # the first one is not shown
            self.dealer_cards.append("a {} {}".
            format(self.dealer_hand[1]["suit"], self.dealer_hand[1]["card"])) 
        else:
            for cards in self.dealer_hand:
                self.dealer_cards.append("a {} {}".
                format(cards["suit"], cards["card"]))
        
        return self.player_cards, self.dealer_cards
    
    # print method which prints the cards of the player(s)/dealer
    def displayHands(self) -> None:
        # if case num_players > 1
            # player_cards will be a 2d array
            # for player in range(num_players):
                # player_cards[player] = [cards["card"] for cards in self.player_hands[player]]
        # for player in range(num_player):
            # print(f"")
        # something like that...
        
        print(f"The player has: {self.cardsToString()[0]}")
        print(f"The dealer has: {self.cardsToString()[1]}")



# Deck instance
# game = Deck([], [])
# game.deal()
# game.displayHands()

# # debugging
# for i in range(20):
#     game.hit("player")
#     game.hit("dealer")
#     game.displayHands()
#     print(i)
