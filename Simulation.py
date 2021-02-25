# really unsafe way to launch the imports folder (do this in an ignored main.py)
exec(open('F:\workspace\Blackjack\imports.py').read()) 

from StartingScreen import StartingScreen
from Game import Game
import time as t
import json

class Simulation:
    def __init__(self, n=None, num_players=1, sim_type="auto_draw_up_to_n", draw_limit=None) -> None:
        self.num_players = num_players # for now we play with 1 player
        self.draw_limit = draw_limit
        self.start = StartingScreen() # the player joins the table
        self.game = Game()
        self.sim_type = sim_type # defaulft is the working simulation for now
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
    def collectGameData(self, sim_type="auto_draw_up_to_n") -> dict:
        # define a simulation boolean
        self.double = True if sim_type == "auto_double" else False
        
        # we create a dictionnary with some unique attributes
        self.auto_game_results = {
            "played": self.played if self.played else 1,
            "sim_type": self.sim_type,
            "draw_limit": self.draw_limit,
            "player_count": self.player_count,
            "games": []
        }
        if (self.double):
            # the results for the games are appended to the games key
            self.sim_results = self.game.autoDraw(self.played, self.double) 
            self.auto_game_results["games"] = self.sim_results
        else:
            self.sim_results = self.game.autoDraw(self.played, self.double, self.draw_limit)
            self.auto_game_results["games"] = self.sim_results
        
        return self.auto_game_results
    
    # 2.1.4
    # method which tracks down the blackjacks in a dataset
    def blackjackCounter(self, data=None, player_count=1) -> int:
        self.dealer_bjs = self.player_bjs = 0
        data = data if data else self.auto_game_results
        
        # we iterate through all games played
        for game in data["games"]:
            if game["player_blackjack"] == True: # or the player/dealer_blackjack values
                self.player_bjs += 1
            
            elif game["dealer_blackjack"] == True: # or the player/dealer_blackjack values
                self.dealer_bjs += 1
        self.total_bjs = self.dealer_bjs + self.player_bjs

        return self.total_bjs
    
    
    # 2.1.5
    # method which counts wins and losses of the player
    def outcomeCounter(self, data=None):
        data = data if data else self.auto_game_results
        self.outcomes = {
            "games_played": self.played,
            "sim_type": self.sim_type,
            "draw_limit": self.draw_limit,
            "win": 0,
            "loss": 0
        }
        # same procedure as for the method before
        for game in data["games"]:
            if game["winner"] == "dealer": # the player lost
                self.outcomes["loss"] += 1
            else:    
                self.outcomes["win"] += 1
        
        # for data printing
        self.wins = self.outcomes["win"]
        self.losses = self.outcomes["loss"]
        # print(f"Out of {self.played} game{self.plural}, the player has won {self.wins} time{self.plural} and loss {self.losses} time{self.plural}.")

        
        return self.outcomes
    
    # 2.1.6
    # method which counts all the possibles outcomes of thee game
    def outcomeTypeCounter(self, data=None) -> dict:
        data = data if data else self.auto_game_results
        self.outcome_type = {
            "sim_typ": self.sim_type,
            "games_played": self.played,
            "won": self.wins,
            "lost": self.losses,
            "draw_limit": self.draw_limit,
            "player_count": 1,
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
        
        # for data printing
        self.busts = self.outcome_type["bust"]
        self.comparison = self.outcome_type["comparison"]
        self.blackjack = self.outcome_type["blackjack"]
        print(f"Out of {self.played} game{self.plural}, the player  {self.wins} time{self.plural} and loss {self.losses} time{self.plural}.")
        
        return self.outcome_type
    
    # 2.1.7
    # method which calculates the times it takes for given operations (for now, exclusively for the ads)
    def takesTime(self, instructions):
        """exec() HIGH RISK"""
        self.start = t.time()
        results = self.collectGameData()
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
    def toJson(self, filepath, data=None):
        data = data if data else self.auto_game_results

        with open(f"data/{filepath}.json", "w") as results:
            json.dump(data, results, indent=2)
        
    """
    (3.1) - Raw data is exported to a mock-results.csv file. 
    """
    # method which exports the raw game data to CSV
    def toCsv(self):
        pass

