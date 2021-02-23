# really unsafe way to launch the imports folder (do this in an ignored main.py)
exec(open('F:\workspace\Blackjack\imports.py').read()) 

from StartingScreen import StartingScreen
from Game import Game
import time as t
import json

class Simulation:
    def __init__(self, num_players=1) -> None:
        self.num_players = num_players # for now we play with 1 player
        self.start = StartingScreen() # the player joins the table
        self.game = Game()
        self.results = ""
    """
    (2.1)  
    - To be able to draw cards automatically up to n points, a autoDraw(self, n) method is added
    written in the Game class. The results are written and stored in the writeResults(self, winner, 
    nature, num_drawn_cards, target=[]) method.
    - Another scenario would be to automate the double-down answers to yes and then to collect
    data.
    """
    def collectRawGameData(self, value, n=None):
        # for the basic scenario
        self.results = self.game.autoDraw(value, n)
        
        # for the double-down scenario
        # coming soon
    """
    (3.x) - Raw data is exported to a mock-results.json file (the data is not valid JSON
    as it is an array of dictionnaries/json data) !
    """
    # method which exports the raw game data to json
    def toJson(self, data=None): 
        # if the data is not given we take the results from simulated games
        data = data if data else self.results
        
        with open("simulation/mock-results.json", "w") as results:
            json.dump(self.results, results, indent=2)
        
    # method which exports the raw game data to CSV
    def toCsv(self):
        pass




# simulations = Simulation()
# simulations.collectRawGameData(15, 50)


# simulations.toJson()
# print(simulations.results)
