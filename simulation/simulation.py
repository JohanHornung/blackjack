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
        self.sim_type = "auto_draw_up_to_n" # hardcoded for now
        self.player_count = 1 # for now
    """
    (2.1)  
    - To be able to draw cards automatically up to n points, a autoDraw(self, n) method is added
    written in the Game class. The results are written and stored in the writeResults(self, winner, 
    nature, num_drawn_cards, target=[]) method.
    - Another scenario would be to automate the double-down answers to yes and then to collect
    data.
    """
    def collectGameData(self, value, n=None):
        # for the basic scenario
        # we create a dictionnary with some unique attributes
        self.auto_draw_id = {
            "num_games": n if n else 1,
            "sim_type": self.sim_type,
            "draw_limit": value,
            "player_count": self.player_count,
            "games": []
        }
        # the results for the games are appended to the games key
        self.sim_results = self.game.autoDraw(value, n) 
        self.auto_draw_id["games"] = self.sim_results
        
        # for the double-down scenario
        # coming soon
    
    # 2.1.4
    # method which tracks down the blackjacks in a dataset
    def blackjackCounter(self):
        pass
    
    # 2.1.5
    # method which tracks down the outcome reason in a dataset
    def outcomeCounter(self):
        pass
    
    """
    (3.1) - Raw data is exported to a mock-results.json file (the data is not valid JSON
    as it is an array of dictionnaries/json data) !
    """
    # method which exports the raw game data to json
    def toJson(self, data=None): 
        # if the data is not given we take the results from simulated games
        data = data if data else self.auto_draw_id
        
        with open("simulation/mock-results.json", "w") as results:
            json.dump(self.auto_draw_id, results, indent=2)
        
    """
    (3.1) - Raw data is exported to a mock-results.csv file. 
    """
    # method which exports the raw game data to CSV
    def toCsv(self):
        pass




simulations = Simulation()
simulations.collectGameData(15, 20)
# print(simulations.sim_id)

simulations.toJson()
# print(simulations.results)
