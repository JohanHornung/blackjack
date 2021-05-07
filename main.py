# main file of the project where everything is beeing executed
from Game import *
from Simulation import *
from Model import *
import pandas as pd
import time as t

# main func
def main(stacks):
    start = t.time()
    models = []
    for mode in ["naive", "random"]:
        # creating a naive simulation
        simulation = Simulation(stacks, mode, 11)
        # creating a random simulation
        # simulation = Simulation(stacks, "random")
        # simulating
        simulation.play()
        # simulation.play()
        # outcome statistics
        # simulation.evaluate()
        simulation.evaluate()
        # modelizing data frames
        simulation.modelisation()
        simulation.export_headers()
        # simulation.modelisation()
        models.append([simulation.df_model, f"{simulation.type}"])
        # simulation.model_comparison(models)
        
    # # training model    
    simulation.train()
    simulation.roc_eval()
    # # letting play the nn
    # print("Changing type...")
    simulation.type = "smart"
    smart_simulation = simulation
    # reset counter and stacks
    simulation.stacks = 10000
    simulation.games_played = 0
    smart_simulation.play()
    smart_simulation.evaluate()
    smart_simulation.modelisation()
    smart_simulation.export_headers()
    models.append([smart_simulation.df_model, f"{smart_simulation.type}"])
    simulation.model_comparison(models)
    # outcome statistics
    # naive_simulation.evaluate()
    # simulation.evaluate()

    end = t.time()
    print("Time elapsed: " + str(round(end - start, 2)) + " seconds")
    print("\n")
    













































if __name__ == "__main__":
    stacks = int(input("How many stacks?\n"))
    main(stacks)