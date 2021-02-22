from StartingScreen import StartingScreen
from Game import Game


class Simulation:
    def __init__(self, num_players=1) -> None:
        self.num_players = num_players # for now we play with 1 player
        self.start = StartingScreen() # the player joins the table
        self.game = Game()
    
    """
    (1.3.1) To be able to draw cards automatically up to n points, a autoDraw(self, n) method is added
    written in the Game class. The results are written and stored in the writeResults(self, winner, 
    nature, num_drawn_cards, target=[]) method.
    
    
    """
