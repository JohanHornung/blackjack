# main file of the project where everything is beeing executed
from Game import *
from Simulation import *
import time as t

# main func
def main(stacks):
    start = t.time()
    # creating a naive and random model/simulation
    naive_simulation = Simulation(stacks, "naive", 11)
    # simulating
    naive_simulation.create()
    # outcome statistics
    naive_simulation.evaluate()
    # modelizing data frames
    naive_simulation.modelisation()
    # print(naive_simulation.total_action)
    print("transition from naive to smart")
    naive_simulation.type = "smart"
    naive_simulation.create()
    end = t.time()
    print("Time elapsed: " + str(end - start))
    print("\n")
    # print("naive simulation: ", naive_simulation.stats)
    # print("\n")
    # print("Random simulation: ", random_simulation.stats)
    
    # print(naive_simulation.df_model)
    













































if __name__ == "__main__":
    stacks = int(input("How many stacks?\n"))
    main(stacks)