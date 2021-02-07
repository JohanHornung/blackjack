import random
import tools

"""
RAPPELS: Jeu finis l´option de split() dans game() et menu()

"""


def game(bet):
    game = True
    split = False
    counter = 1
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4

    # Cette boucle est interrompue lorsque le dealer/joueur a un BJ ou > 21
    while game:
        # On tire 2 cartes
        main_joueur = tools.deal(deck)
        # On calcule les valeurs
        valeur_joueur = tools.valeur(main_joueur)

        # On donne 2 cartes au dealer

        main_dealer = tools.deal(deck)
        valeur_dealer = tools.valeur(main_dealer)

        # On affiche une des cartes du dealer (la dernière)

        print("The dealer has X and {}\n".format(main_dealer[1]))

        # On verifie si le dealer a un Blackjack

        blackjack = tools.blackjack(valeur_dealer)
        if blackjack == 1:
            print("The dealer has a Blackjack ! You loose !\n")
            resultat = "perdu"
            game = False

        # On affiche la main du joueur et sa valeur

        tools.display_cards(main_joueur, valeur_joueur)

        # On verifie si le joueur a un Blackjack

        blackjack = tools.blackjack(valeur_joueur)

        if blackjack == 1:
            print("Congratulations, you have a Blackjack !\n")
            resultat = "blackjack"
            game = False
            break

        if valeur_joueur > 21:
            game = False
            print("You busted ! The bank wins.\n")
            resultat = "perdu"

            break

        # On propose au joueur de doubler

        
        double = input("Do you want to double ? (Y/N)\n").lower()
        if double == "y":
            bet *= 2
            tools.hit(main_joueur, deck)
            valeur_joueur = tools.valeur(main_joueur)
            tools.display_cards(main_joueur, valeur_joueur)
            print("The dealer has {} wich gives him a total of {} points.\n".format(main_dealer, valeur_dealer))

            if valeur_joueur > 21:
                game = False
                print("You busted ! The bank wins.\n")
                resultat = "perdu"
                break

            resultat = tools.comparaison(valeur_dealer, valeur_joueur)
            montant = tools.bet(resultat, bet)
            
            if resultat == "draw":
                print("You have as many points as the dealer! You get back your bet.\n")

            elif resultat == "gagne":
                print("Congratulations ! You have more points than the dealer !\n")

            elif resultat == "perdu":
                print("The dealer has more points than you ! You loose !\n")
            
            break

        
        # On propose au joueur de "splitter" ces cartes
        if main_joueur[0] == main_joueur[1]:
            split = input("Do you want to split your deck? (Y/N)\n").lower()

            if split == "y":
                split = True
                bet *= 2
                main_joueur = tools.split(main_joueur)
                main_premiere = []
                main_seconde = []
                #/D print("{}{}\n".format(main_joueur, valeur_joueur))
                
                for i,j in enumerate(main_joueur):
                    if i // 2 == 0:
                        main_premiere.append(j)
                    else:
                        main_seconde.append(j)
                    
                    for card in main_premiere:
                        if card == 11:
                            card = "Jack"
                        elif card == 12:
                            card = "Queen"
                        elif card == 13:
                            card = "King"
                        elif card == 14:
                            card = "Ace"

                    for card in main_seconde:
                        if card == 11:
                            card = "Jack"
                        elif card == 12:
                            card = "Queen"
                        elif card == 13:
                            card = "King"
                        elif card == 14:
                            card = "Ace"
                
                print("Your first deck: {} || Your second deck: {}\n".format(main_premiere, main_seconde))
                answer = str(
                    input("Do you want to hit, stay or switch? (hit/stay/switch)\n")).lower()
                
                while answer == "hit" or answer == "h":
                    tools.hit(main_premiere, deck)
                    valeur_premiere = tools.valeur(main_premiere)
                    tools.display_cards(main_premiere, valeur_premiere)

                    # Si la première main du joueur passe les 21 pts.:
                    if valeur_joueur > 21:
                        bet /= 2 # La moitié de la mise est perdu
                        valeur_seconde = tools.valeur(main_seconde) # Sinon la variable n´éxistera pas 

                        # On affiche un message et on passe à la 2ème main
                        print("You first hand busted ! Let´s go for the another one.\n")
                        continue    
                    
                    answer = str(
                        input("Do you want to hit or stay? (hit/stay)\n")).lower()

                # Á ce point, le joueur a décidé de plus jouer/changer de main ou a passer les 21 pts.           
                if (answer == "switch" or answer == "stay"):
                        print("Let´s play on the second hand:\n")
                        tools.display_cards(main_seconde, valeur_seconde)
                        
                        answer = str(
                            input("Do you want to hit or stay? (hit/stay)\n")).lower()

                        while answer == "hit" or answer == "h":
                            tools.hit(main_seconde, deck)
                            valeur_seconde = tools.valeur(main_seconde)
                            tools.display_cards(main_seconde, valeur_seconde)
                            
                            if valeur_seconde > 21:
                                resultat = "perdu"
                                print("You busted ! The bank wins.\n")
                                break
                                
                            answer = str(
                                input("Do you want to hit, stay or switch? (hit/stay/switch)\n")).lower()
                        break
                
                # Si jamais le joueur ne joue sur aucun de ses cartes
                break
                
        
        answer = str(
            input("Do you want to hit or stay ?(hit/stay)\n\n")).lower()

        while answer == "hit" or answer == "h":
            tools.hit(main_joueur, deck)
            valeur_joueur = tools.valeur(main_joueur)
            tools.display_cards(main_joueur, valeur_joueur)

            if valeur_joueur > 21:
                game = False
                resultat = "perdu"
                print("You busted ! The bank wins\n")
                break

            answer = str(
                input("Do you want to hit or stay ? (hit/stay)\n")).lower()

        if game:
            # Si le dealer a deja plus que 17
            if valeur_dealer >= 17:
                print("The dealer has {} wich gives him a total of {}\n".format(
                    main_dealer, valeur_dealer))

            while valeur_dealer < 17:
                tools.hit(main_dealer, deck)
                valeur_dealer = tools.valeur(main_dealer)

                print("The dealer has {} wich gives him a total of {}\n".format(
                    main_dealer, valeur_dealer))

            if valeur_dealer > 21:
                print("The dealer busted ! You win !\n")
                resultat = "gagne"
                game = False
                break

            # On compare les valeurs pour déterminer le gagnant:

            if not split:
                resultat = tools.comparaison(valeur_dealer, valeur_joueur)

            # Si le joueur a decide de splitter, 2 comparaions sont a faire et la mise a été doublé
            
            # Résultat de comparaison si la fin n´est pas 'spéciale'
            if resultat == "draw":
                print("You have as many points as the dealer! You get back your bet.\n")

            elif resultat == "gagne":
                print("Congratulations ! You have more points than the dealer !\n")

            elif resultat == "perdu":
                print("The dealer has more points than you ! You loose !\n")
            
            game = False
            break

    if split:
        resultat1 = tools.comparaison(valeur_dealer, valeur_premiere)
        resultat2 = tools.comparaison(valeur_premiere, valeur_seconde)
        
        montant = tools.bet(resultat1, bet) + tools.bet(resultat2, bet)
        

    else:
        montant = tools.bet(resultat, bet)

    return montant
