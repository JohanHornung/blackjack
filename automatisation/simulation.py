# for avoiding import conflicts
import sys
sys.path.append("f:\\workspace\\Blackjack\\")

from StartingScreen import StartingScreen


"""
To be able to draw cards automatically up to n points, a autoDraw(self, n) method is added
to a new Simulation class.
"""

class Simulation:
    def __init__(self, num_players=1) -> None:
        self.num_players = num_players # for now we play with 1 player
        self.start = StartingScreen() # the player joins the table
        self.winner = ""
        self.reason = ""

