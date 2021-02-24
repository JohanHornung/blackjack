# really unsafe way to launch the imports folder (do this in an ignored main.py)
exec(open('F:\workspace\Blackjack\imports.py').read()) 

from StartingScreen import StartingScreen
from Game import Game
import time as t
import json

class Simulation:
    def __init__(self, n=None, num_players=1) -> None:
        self.num_players = num_players # for now we play with 1 player
        self.start = StartingScreen() # the player joins the table
        self.game = Game()
        self.sim_type = "auto_draw_up_to_n" # hardcoded for now
        self.player_count = 1 # for now
        self.played = n if n else 1
        # plural handeling
        self.plural = "s" if self.played > 1 else ""

    """
    (2.1)  
    - To be able to draw cards automatically up to n points, a autoDraw(self, n) method is added
    written in the Game class. The results are written and stored in the writeResults(self, winner, 
    nature, num_drawn_cards, target=[]) method.
    - Another scenario would be to automate the double-down answers to yes and then to collect
    data.
    """
    def collectGameData(self, value) -> dict:
        # for the basic scenario
        # we create a dictionnary with some unique attributes
        self.auto_draw_results = {
            "played": self.played if self.played else 1,
            "sim_type": self.sim_type,
            "draw_limit": value,
            "player_count": self.player_count,
            "games": []
        }
        # the results for the games are appended to the games key
        self.sim_results = self.game.autoDraw(value, self.played) 
        self.auto_draw_results["games"] = self.sim_results
        
        # for the double-down scenario
        # coming soon
    
        return self.auto_draw_results
    # 2.1.4
    # method which tracks down the blackjacks in a dataset
    def blackjackCounter(self, data=None, player_count=1) -> int:
        self.dealer_bjs = self.player_bjs = 0
        data = data if data else self.auto_draw_results
        
        # we iterate through all games played
        for game in data["games"]:
            if game["player_blackjack"] == True: # or the player/dealer_blackjack values
                self.player_bjs += 1
            
            elif game["dealer_blackjack"] == True: # or the player/dealer_blackjack values
                self.dealer_bjs += 1
        self.total_bjs = self.dealer_bjs + self.player_bjs

        return self.total_bjs
    
    # 2.1.5
    # method which counts all the possibles outcomes of thee game
    def outcomeTypeCounter(self, data=None) -> dict:
        data = data if data else self.auto_draw_results
        self.outcome_type = {
            "games_played": self.played,
            "comparison": 0,
            "bust": 0,
            "blackjack": 0,
        }
        # iteration through the game results
        for game in data["games"]:
            # handleling all different outcome_type
            if game["type"] == "bust":
                self.outcome_type["bust"] += 1
            elif game["type"] == "blackjack":
                self.outcome_type["blackjack"] += 1
            else:    
                self.outcome_type["comparison"] += 1

        print(f"Out of {self.played} game{self.plural} \
            , the player has won {self.wins} time{self.plural} and loss {self.losses} time{self.plural}.")
        return self.outcome_type
    
    # 2.1.6
    # method which counts wins and losses of the player
    def outcomeCounter(self, data=None):
        data = data if data else self.auto_draw_results
        self.outcomes = {
            "games_played": self.played,
            "win": 0,
            "loss": 0
        }
        # same procedure as for the method before
        for game in data["games"]:
            if game["winner"] == "dealer": # the player lost
                self.outcomes["loss"] += 1
            else:    
                self.outcomes["win"] += 1
        
        self.wins = self.outcomes["win"]
        self.losses = self.outcomes["loss"]
        print(f"Out of {self.played} game{self.plural}, the player has won {self.wins} time{self.plural} and loss {self.losses} time{self.plural}.")

        
        return self.outcomes
    
    # 2.17
    # method which calculates the times it takes for given operations (for now, exclusively for the ads)
    def takesTime(self, instructions, value, n):
        """exec() HIGH RISK"""
        self.start = t.time()
        results = simulations.collectGameData(value, n)
        # this method needs to be avoided
        for instruction in instructions:
            exec(instruction)
        
        self.end = t.time()
        self.time = (self.end - self.start)
        
        return self.time    
    
    """
    (3.1) - Raw data is exported to a mock-results.json file (the data is not valid JSON
    as it is an array of dictionnaries/json data) !
    """
    # method which exports the raw game data to json
    def toJson(self, filename, data=None):
        data = data if data else self.auto_draw_results

        with open(f"data/{filename}.json", "w") as results:
            json.dump(data, results, indent=2)
        
    """
    (3.1) - Raw data is exported to a mock-results.csv file. 
    """
    # method which exports the raw game data to CSV
    def toCsv(self):
        pass



simulation = Simulation(300)
instructions = ["simulation.toJson('mock-results-autodraw', results)"]
simulation.collectGameData(15)
simulation.outcomeCounter()
simulation.toJson("outcomes", simulation.outcomes)
simulation.toJson("mock-results-autodraw")
# print(simulations.takesTime(instructions, 15, 500))
# print(then-now)
# print(results)

# outcome_type = simulations.outcomeTypeCounter(results)
# # print(outcome_type)
# outcomes = simulations.outcomeCounter()
# simulations.toJson("outcome_type", outcome_type)
# simulations.toJson("outcomes", outcomes)
# print(simulations.total_bjs)
