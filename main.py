# main file of the project where everything is beeing executed
from Game import *
from Simulation import *
from Model import *
import numpy
import pandas as pd
import time as t

# main func
def main(stacks):
    start = t.time()
    models = []
    # creating a naive simulation
    random_simulation = Simulation(stacks, "random")
    # creating a random simulation
    # random_simulation = Simulation(stacks, "random")
    # simulating
    random_simulation.play()
    # random_simulation.play()
    # outcome statistics
    # random_simulation.evaluate()
    random_simulation.evaluate()
    # modelizing data frames
    random_simulation.modelisation()
    # random_simulation.modelisation()
    models.append([random_simulation.df_model, f"{random_simulation.type}"])
    # random_simulation.model_comparison(models)
    
    # training model    
    random_simulation.train()
    random_simulation.roc_eval()
    # # letting play the nn
    # print("Changing type...")
    random_simulation.type = "smart"
    smart_simulation = random_simulation
    smart_simulation.play()
    smart_simulation.evaluate()
    smart_simulation.modelisation()
    smart_simulation.export_headers()
    # models.append([smart_simulation.df_model, f"{smart_simulation.type}"])
    # outcome statistics
    # naive_simulation.evaluate()
    # random_simulation.evaluate()

    end = t.time()
    print("Time elapsed: " + str(round(end - start, 2)) + " seconds")
    print("\n")
    













































if __name__ == "__main__":
    stacks = int(input("How many stacks?\n"))
    main(stacks)