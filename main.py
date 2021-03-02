# exec(open("F:\workspace\Blackjack\imports.py").read())
from Simulation import Simulation

def main():
    simulation = Simulation(5, 1, "auto-double")
    instructions = ["simulation.toJson('mock-results-autodraw', results)"]
    # print(simulation)
    # print(simulation.takesTime(instructions))
    # simulation.collectGameData("auto_double")
    # print(simulation.auto_game_results)
    # simulation.toJson("auto-double/mock-results-auto-double", simulation.auto_game_results)    
    # simulation.outcomeCounter()
    # simulation.outcomeTypeCounter()
    # simulation.toJson("auto-double/outcome_type", simulation.outcome_type)
    # simulation.toJson("auto-double/outcomes", simulation.outcomes)
    # # simulation.toJson("auto-draw-up-to-n/mock-results-autodraw")
    # print(simulations.takesTime(instructions, 15, 500))
    # print(results)

    # outcome_type = simulations.outcomeTypeCounter(results)
    # # print(outcome_type)
    # outcomes = simulations.outcomeCounter()
    # simulations.toJson("outcomes", outcomes)
    # print(simulations.total_bjs)





if "__main__" == __name__:
    main()