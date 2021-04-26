# really unsafe way to launch the imports folder (do this in an ignored main.py)
# exec(open('F:\workspace\Blackjack\imports.py').read()) 

from StartingScreen import StartingScreen
from Game import Game
from config import *
import time as t
import json
import csv

class Simulation:
    def __init__(self, n=None, num_players=1, sim_type="auto_draw_up_to_n", draw_limit=None):
        self.num_players = num_players # for now we play with 1 player
        self.draw_limit = draw_limit
        self.start = StartingScreen() # the player joins the table
        self.game = Game()
        self.sim_type = sim_type # 3 simulation types for now
        self.player_count = 1 # for now
        self.played = n if n else 1
        # plural handeling
        self.plural = "s" if self.played > 1 else ""
        self.auto_game_results = ""
        # self.tracked_cards = []

    """
    (2.1)  
    - To be able to draw cards automatically up to n points, a autoDraw(self, n) method is added
    written in the Game class. The results are written and stored in the writeResults(self, winner, 
    nature, num_drawn_cards, target=[]) method.
    - Another scenario would be to automate the double-down answers to yes and then to collect
    data.
    """
    def collectGameData(self):
        # define a simulation boolean
        self.double = True if self.sim_type == "auto_double" else False
        
        # we create a dictionnary with some unique attributes
        self.auto_game_results = {
            "played": self.played if self.played else 1,
            "sim_type": self.sim_type,
            "draw_limit": self.draw_limit,
            "player_count": self.player_count,
            "games": []
        }
        # launching the different simulation types
        if (self.double):
            # the results for the games are appended to the games key
            self.sim_results = self.game.autoDraw(self.played, self.sim_type) 
            self.auto_game_results["games"] = self.sim_results
        
        elif (self.sim_type == "auto_draw_up_to_n"):
            self.sim_results = self.game.autoDraw(self.played, self.sim_type, self.draw_limit)
            self.auto_game_results["games"] = self.sim_results
        
        elif (self.sim_type == "one_hit"):
            self.sim_results = self.game.autoDraw(self.played, self.sim_type)
            self.auto_game_results["games"] = self.sim_results
        # return self.auto_game_results
    
    # 2.1.4
    # method which tracks down the blackjacks in a dataset
    def blackjackCounter(self, data=None, player_count=1):
        data = data if data else self.auto_game_results
        self.dealer_bjs = self.player_bjs = 0
        
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
            "loss": 0,
            "draw": 0,
        }
        # same procedure as for the method before
        for game in data["games"]:
            
            if game["winner"] == "dealer": # the player lost
                self.outcomes["loss"] += 1
            elif game["winner"] == "player":    
                self.outcomes["win"] += 1
            else: # draw
                self.outcomes["draw"] += 1
        
        # for data printing
        self.wins = self.outcomes["win"]
        self.losses = self.outcomes["loss"]
        self.draws = self.outcomes["draw"]
        # print(f"Out of {self.played} game{self.plural}, the player has won {self.wins} time{self.plural} and loss {self.losses} time{self.plural}.")

        return self.outcomes
    
    # 2.1.6
    # method which counts all the possibles outcomes of thee game
    def outcomeTypeCounter(self, data=None):
        data = data if data else self.auto_game_results
        self.outcome_type = {
            "sim_typ": self.sim_type,
            "games_played": self.played,
            "win": self.wins,
            "loss": self.losses,
            "draw": self.draws,
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
        # print(f"Out of {self.played} game{self.plural}, the player  {self.wins} time{self.plural} and loss {self.losses} time{self.plural}.")
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
        
        return round(self.time, 1)    
    
    """
    (3.1) - Raw data is exported to a mock-results.json file (the data is not valid JSON
    as it is an array of dictionnaries/json data) !
    """
    # method which exports the raw game data to json
    def toJson(self, filepath, data=None):
        data = data if data else self.auto_game_results
        with open(f"data/JSON/{filepath}.json", "w") as results:
            json.dump(data, results, indent=2)
        print(f"data sucessfully exported to {filepath}.json")
    """
    (3.1) - Raw data is exported to a mock-results.csv file. 
    """
    # for the auto-double/draw the data, 2 files will be created
    # method which exports the raw game data id to CSV
    def idToCsv(self, filepath, data=None):
        data = data if data else self.auto_game_results
        # frist file: the fieldnames are the simulation infos (not the games themselfs)
        with open(f"data/CSV/{filepath}.csv", "w", newline="") as id_results:
            self.outcomeCounter(data) # for more data 
            self.outcomeTypeCounter(data) # for more data
            data.pop("games") # as the games are not in the first file
            self.id_fieldnames = [key for key in self.outcome_type.keys()]
            # id_writer objects for the games 
            self.id_writer = csv.DictWriter(id_results, fieldnames=self.id_fieldnames)
            self.id_writer.writeheader()
            self.id_writer.writerow(self.outcome_type)

        print(f"data sucessfully exported to {filepath}.csv")
    
    def contentToCsv(self, filepath, data=None):
        data = data if data else self.auto_game_results
        # second file: the fieldnames are (not the games themselfs)
        with open(f"data/CSV/{filepath}.csv", "w", newline="") as cont_results:
            self.games = data.pop("games") # as the games are not in the first file
            self.content_fieldnames = [key for key in self.games[0].keys()]
            
            # content_writer objects for the games 
            self.content_writer = csv.DictWriter(cont_results, fieldnames=self.content_fieldnames)
            self.content_writer.writeheader()
            for games in self.games:
                self.content_writer.writerow(games)
    
        print(f"data sucessfully exported to '{filepath}.csv'")

    # method which caculates all cain of statistics about the simulated game results
    def statistics(self):
    
        # statistic dictionnary which will be treated on each game
        self.data_statistics = {
            "total_games": self.played,
            "total_cards": len(self.game.stat_cards), # param_value
            "draw_limit": self.draw_limit,
            "win": 0,
            "loss": 0,
            "draw": 0,
            "blackjack": 0,
            "bust": 0,
            "comparison": 0,
            "cards": {
                "pictured_cards": 0,
                "numbered_cards": 0,
                "suits": {
                    "spades": 0,
                    "hearts": 0,
                    "diamonds": 0,
                    "clubs": 0,
                },
                "aces": 0,
                "queens": 0,
                "kings": 0,
                "jacks": 0,
                "tens": 0,
                "nines": 0,
                "eights": 0,
                "sevens": 0,
                "six": 0,
                "fives": 0,
                "fours": 0,
                "threes": 0,
                "twos": 0,
            }
        }
        # for defining number of wins and additional data
        self.outcomes = self.outcomeCounter(self.auto_game_results)
        self.outcome_type = self.outcomeTypeCounter(self.auto_game_results)
        
        # function which returns specific statistical value in relation to a specific parameter
        def outcomeStatistic(data, key, param):
            outcome_value = data.get(key, None)
            # param_value = data.get(param, None)
            # check for presence of the data
            if (outcome_value != None and param != None):
                result = round(outcome_value / param, 3)
                return result
            else:
                return None
        
        # setting the outcome type for now
        self.categories = ["general", "cards"]
        # self.param_outcome = ["games_played"]
        # function which inserts a caclulated statistic value of given keys
        def keyFill(category, data):
            # if general statistics are filled out
            if category == "general": # filling out general information
                for key in ["blackjack", "win", "loss", "draw", "comparison", "bust"]:
                    data[key] = outcomeStatistic(self.outcome_type, key, self.played)
            
            elif category == "cards": # filling out statistics about cards themselfs
                total_cards = len(self.game.stat_cards)
                pictured_cards = 0
                numbered_cards = 0
                # looking into the drawn cards
                for card in self.game.stat_cards:
                    # check the card for beeing an image or a number
                    # the image has a value of at least 10 (value of ace in id alays == 11)
                    if (card["value"] >= 10 and card["card"] != "Ten"):
                        pictured_cards += 1 
                        # check the images
                        if (card["card"] == "King"):
                            data["cards"]["kings"] += 1
                        elif (card["card"] == "Queen"):
                            data["cards"]["queens"] += 1
                        elif (card["card"] == "Ace"):
                            data["cards"]["aces"] += 1
                        else:
                            data["cards"]["jacks"] += 1
                    else:
                        numbered_cards += 1
                        # check the numbers
                        if (card["card"] == "Ten"):
                            data["cards"]["tens"] += 1
                        elif (card["card"] == "Nine"):
                            data["cards"]["nines"] += 1
                        elif (card["card"] == "Eight"):
                            data["cards"]["eights"] += 1
                        elif (card["card"] == "Seven"):
                            data["cards"]["sevens"] += 1
                        elif (card["card"] == "Six"):
                            data["cards"]["six"] += 1
                        elif (card["card"] == "Five"):
                            data["cards"]["fives"] += 1
                        elif (card["card"] == "Four"):
                            data["cards"]["fours"] += 1
                        elif (card["card"] == "Three"):
                            data["cards"]["threes"] += 1
                        elif (card["card"] == "Two"):
                            data["cards"]["twos"] += 1

                    # checking the suits
                    if (card["suit"] == "hearts"):
                        data["cards"]["suits"]["hearts"] += 1
                    elif (card["suit"] == "spades"):
                        data["cards"]["suits"]["spades"] += 1
                    elif (card["suit"] == "diamonds"):
                        data["cards"]["suits"]["diamonds"] += 1
                    else:
                        data["cards"]["suits"]["clubs"] += 1

                # filling out
                for key in SUITS:
                    data["cards"]["suits"][key] = outcomeStatistic(self.data_statistics["cards"]["suits"], key, total_cards)
                
                # for suit in SUITS:
                #     data["cards"]["suits"][suit] = round(data["cards"]["suits"][suit] / total_cards, 3)
                
                cards = ["aces", "queens", "kings", "jacks", "tens", "nines", "eights", "sevens", "six", "fives", "fours", "threes", "twos"]
                for card in cards:
                    data["cards"][card] = round(data["cards"][card] / total_cards, 3)
                
                for key in ["pictured_cards", "numbered_cards"]:
                    data["cards"][key] = outcomeStatistic(self.data_statistics["cards"], key, total_cards)
                
            
        keyFill(self.categories[0], self.param_outcome[0], self.data_statistics) # for general stats
        keyFill(self.categories[1],self.param_outcome[1], self.data_statistics) # for card stats

    # method which evaluates the move from the player for the one hit simulation 
    def evaluate(self):
        # the correctness is represented by an array of 1's or 0's
        self.right_decision = []
        
        for game in self.auto_game_results["games"]:
            self.index = game["game"] - 1 # nth game - 1 for array index
            if (game["winner"] == "player"):
                # if the player hits and wins, the hit was a correct decision (C=1) 
                if game["decision"] == "hit":
                    self.right_decision[self.index] = 1
                else:
                    # if the player stays and wins, the stay was a good decision (C=1) 
                    self.right_decision[self.index] = 0

            else:
                # if the player stays and loses, the stay was a good decision (C=1) 
                if game["decision"] == "stand":
                    self.right_decision[self.index] = 1
                # if the player hits and loses, the hit was a bad decision (C=0) 
                else:
                    self.right_decision[self.index] = 0



# debugging 
simulation = Simulation(10, 1, "one_hit")
simulation.collectGameData()
simulation.outcomeCounter()
simulation.outcomeTypeCounter()
simulation.toJson("one_hit/one_hit_mock", simulation.auto_game_results)
# simulation.statistics()
# print(simulation.game.stat_cards)
# print(simulation.data_statistics)
# simulation.statistics()
# simulation.contentToCsv("content-mock") 
# simulation.idToCsv("id-mock-csv")
# print(simulation.tracked_cards)
# print(simulation.sim_results)
# print(simulation.auto_game_results)
# print(simulation.fieldnames)
