# main file of the project where everything is beeing executed
from Game import *
from Simulation import *
import time as t

# main func
def main(stacks):
    start = t.time()
    # creating a smart and random model/simulation
    smart_simulation, random_simulation = Simulation(stacks, "smart"), Simulation(stacks, "random")
    # simulating
    smart_simulation.create()
    random_simulation.create()
    # outcome statistics
    smart_simulation.evaluate()
    random_simulation.evaluate()
    # modelizing data frames
    smart_simulation.modelisation()
    random_simulation.modelisation()
    # visualizing
    smart_simulation.player_value_impact("Player´s value", "Probability of win or tie")
    random_simulation.player_value_impact("Player´s value", "Probability of win or tie")
    smart_simulation.first_dealer_card_impact("Dealers first card", "Probability of win or tie")
    random_simulation.first_dealer_card_impact("Dealers first card", "Probability of win or tie")
    smart_simulation.heatmap("Player´s hand value", "Dealer´s card")
    random_simulation.heatmap("Player´s hand value", "Dealer´s card")
    # comparing
    smart_simulation.model_comparison(random_simulation.df_model)
    # exporting headers
    smart_simulation.export_headers()
    random_simulation.export_headers()

    end = t.time()
    print("Time elapsed: " + str(end - start))
    print("\n")
    # print("Smart simulation: ", smart_simulation.stats)
    # print("\n")
    # print("Random simulation: ", random_simulation.stats)
    
    # print(smart_simulation.df_model)
    













































if __name__ == "__main__":
    stacks = int(input("How many stacks?\n"))
    main(stacks)