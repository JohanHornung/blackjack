import game


"""
Menu principal ou le joueur aura le choix de jouer plusieurs parties ou
de deposer son argent en quittant. (le système de mise a été transférer
vers le menu)
"""


def menu():
    banque = 0
    answer = ""
    resultat = ""
    rounds = 0
    
    # boucle pour éviter les erreurs d´options
    while True: 
        try:
            action = input(
            """ Welcome to Blackjack (Las Vegas type), please choose an option:\n\n
                ||  1 --> Play  ||  2 --> Whitdraw money and quit  || \n\n
                Blackjack pays 3:2 (as a bonus) ||| A 'normal' win pays 2:1\n""")

        # Si le input du joueur n´est pas un numéro, la demande se répète
        except (ValueError):
            print("This isn´t a number!\n")
            continue
        

        # Option de créateur si un mot de passe et tapez la partie est gagngé
        """if action == "salut":
            resultat = "gagne"
            continue"""
                
        action = int(action)
        # Si le joueur décide de quitter:
        if action == 2:
            if banque == 0 and rounds == 0: # Si jamais le joueur n´a pas jouer avant:
                print(
                    "\nNothing has been added to your bank account as you haven´t played yet!\n")
                break

        elif action != (1 or 2):    # Si l´input du joueur n´est pas 1 ni 2
            print("\nThis isn´t an option !\n")
        
        if action == 1: # On sort de la boucle pour commencer à jouer   
            break
    
    while action == 1 or answer == "y":
        # À ce point, le joueur a decider de jouer    
        if rounds == 0:
            amount = int(
                    input("How much money do yout want to deposit ?\n"))
            banque += amount
        
        mise = input("Your bets please\n")
            
        if mise == "all in":
            mise = banque
            print("Ok so you go 'all in', {} $ on this game.\n".format(mise))
        else:
            mise = int(mise)
        
        if mise > banque:
            print("Sorry but you have not enough money !\n")
            continue
        
        rounds += 1
        # On joue le jeu en soustraient et en ajoutant le montant brute gagné à la banque 
        banque -= mise
        money = game.game(mise)
        banque += money

        print("After {} round(s), you have currently {} $ in your bank account.\n".format(rounds, banque))

        # Si le joueur n´a plus d´argent, le programme s´arrete
        if banque == 0:
            print(
                "As you already noticed, you don´t have money to play with ! Goodbye\n")
            break
        
        # L´option de rejouer
        answer = str(input("Do you want to play again? (Y/N)\n")).lower()
        
        # Si l´utilisateur décide de ne plus jouer
        if answer[0] != "y":
            print("After {} round(s), {} $ have been added to your bank account. Goodbye.\n".format(rounds, banque))
            break

            
if __name__ == "__main__":
    menu()
