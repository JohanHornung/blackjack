# main file of the project where everything is beeing executed
from Game import *
from Simulation import *
from Model import *
import time as t

# main func
def main(stacks):
    start = t.time()
    models = []
    # creating a naive simulation
    naive_simulation = Simulation(stacks, "naive", 11)
    # creating a random simulation
    random_simulation = Simulation(stacks, "random")
    # simulating
    naive_simulation.play()
    random_simulation.play()
    # outcome statistics
    naive_simulation.evaluate()
    random_simulation.evaluate()
    # modelizing data frames
    naive_simulation.modelisation()
    random_simulation.modelisation()
    models.append([naive_simulation.df_model, f"{naive_simulation.type}"])
    models.append([random_simulation.df_model, f"{random_simulation.type}"])
    
    # outcome statistics
    naive_simulation.evaluate()
    random_simulation.evaluate()
    # comparing
    # naive_simulation.model_comparison(models, "mocks")
    # print("training...")
    naive_simulation.train()
    naive_simulation.roc_eval()

    end = t.time()
    print("Time elapsed: " + str(round(end - start, 2)) + " seconds")
    print("\n")
    













































if __name__ == "__main__":
    stacks = int(input("How many stacks?\n"))
    main(stacks)