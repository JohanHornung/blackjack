# main file of the project where everything is beeing executed
from Game import *
from Simulation import *
from Model import *
import time as t

# main func
def main(stacks, num_epochs, coeff):
    start = t.time()
    models = []
    total_stats = []
    for mode in ["naive"]:
        # creating a naive simulation
        simulation = Simulation(stacks, coeff, num_epochs, mode, 11)
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
        # simulation.heatmap("Valeur de main", "Première cart du croupier")
        simulation.export_headers()
        total_stats.append(simulation.stats)
        # simulation.export_headers()
        # simulation.modelisation()
        models.append([simulation.df_model, f"{simulation.type}"])
        # simulation.model_comparison(models)
        # print(simulation.df_model)
    # training model    
    simulation.train()
    simulation.roc_eval()
    # letting play the nn
    print("Changing type...")
    simulation.type = "smart"
    # reset counter and stacks (more vars need to be reset)
    simulation.reset(75000)
    simulation.play()
    simulation.evaluate()
    simulation.modelisation()
    simulation.export_headers()
    models.append([simulation.df_model, f"{simulation.type}"])
    total_stats.append(simulation.stats)    
    # comparing
    simulation.hit_frequency()
    # simulation.model_comparison(models, total_stats)

    end = t.time()
    print("Time elapsed: " + str(round(end - start, 2)) + " seconds")
    print("\n")
    



if __name__ == "__main__":
    stacks = int(input("How many stacks?\n"))
    num_epochs = int(input("How many epochs for training?\n"))
    coeff = float(input("Minimum prediction accuracy?\n"))
    main(stacks, num_epochs, coeff)