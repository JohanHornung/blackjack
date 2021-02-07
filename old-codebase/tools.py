import random

"""
- Ce fichier est simplement un répertoire de fonction pour notre jeu comme par exemple
pour la distribution de cartes, le calcul de leur valeur, un booléen pour un 'Blackjack' etc.

- 'functions.py' sera ensuite utilisé comme module pour le menu() principal et pour le fichier
game() (qui sera le jeu en soit) c´est à dire qu´on importera son contenu donc toutes ses fonctions
icomprises. Ceci évite des réptitions du même bout de code. Cette technique nous permettera une syntaxe
plus propre et compréhensible.
"""

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
symbole = ["♥", "♦", "♣", "♠"]*13



"""
- Cette fonction sert à distribuer 2 cartes pour le début de la partie, la méthode pop() est ici utilisé,
elle renvoie une carte du deck et la supprime automatiquement de deck de jeu pour éviter que la même carte
est tirée 2 fois. De même, elle convertit les valeurs de 11 à 14 aux images correspondants.

- Cette fonction a comme arguments le deck utilisé au Blackjack (52 cartes donc 4 decks).  
"""


def deal(deck):
    hand = []  # main vide
    # mélange les cartes
    random.shuffle(deck)
    # le joueur recoit 2 cartes
    for j in range(2):
        # on prend au hasard une carte
        card = deck.pop()  # Cette carte sera ensuite enlevé du deck[]
        # on détermine les valeurs des “images”, pour ensuite les convertir en leur valeur
        if card == 11:
            card = "Jack"
        elif card == 12:
            card = "Queen"
        elif card == 13:
            card = "King"
        elif card == 14:
            card = "Ace"
        # on ajoute les cartes à la main
        hand.append(card)
        # hand.append(symbole.pop())
    
    return hand  # On renvoie la main pour ensuite continuer à joueur avec cette liste


"""
- Un total est défénit pour lui ajouter au cours de cette fonction les valeurs
des cartes. Pour calculer la valeur pour chaque carte dans la main du joueur
et du dealer on itère la main du joeur. Ici, la variable 'card' peut prendre la valeur :
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King, "Ace"] à chaque passage. Le nombre
de tour est définie par la taille de la liste (la main de nos joueurs).

NOTICE: Dans ce procés, l´As peut admettre 2 valeurs par rapport au jeu que le joueur a. (1 ou 11)
Une résolution/condition trop simple de ce problème aurait posé problème au cours de l´algorithme.

- Cette fonction a comme arguments la main des joueurs pour évaluer sa valeur. 
"""


def valeur(hand):
    total = 0
    # itération dans la main du joueur (liste)
    for card in hand:
        # L´as peut avoir 2 valeur: 1 ou 11
        # Si le total + card > 21, l´As = 1
        """if card == ('♥' or '♦' or '♣' or '♠'):
            break"""
        if card == "Ace":
            if total > 21:
                total += 1
            else:  # Sinon l´As = 11
                total += 11
        # Si une des cartes est une "image"
        elif card == "Jack" or card == "Queen" or card == "King":
            # tous les 4 symboles ont la même valeur
            total += 10
        # Si aucune des cartes est une 'image'
        else:
            total += card  # Puisque la carte aura une valeur de 1 à 10

    """
    Si le total > 21 il faut regarder si le joueur a un As dans la main,
    si ceci est le cas, l´As = 1 donc on soustrait 10 à la valeur totale.
    """
    if total > 21:
        for card in hand:
            if card == "Ace":
                total -= 10

    return total


"""
- Cette fonction affche les cartes du joueur et leurs valeurs.
- Cette fonction a comme arguments la main et sa valeur des joueurs.
"""


def display_cards(deck, value):
    print("You have {} wich gives you a total of {} points.\n".format(deck, value))


"""
- Cette fonction fait tirer au joueur une autre carte grace à la fonction pop(),qui elle renvoit une carte
 au hasard et la supprime du deck. Celle ci est sauvegardé dans la variable 'card', elle est directement 
 convertit en images et est ajouté à la main du joueur.

- Cette fonction a comme arguments la main du joueur et le deck utilisé pour le jeu Blackjack. 
"""


def hit(main, deck):
    # on prend au hasard une carte
    card = deck.pop()
    # on détermine les valeurs des “images”:
    if card == 11:
        # pour ensuite les convertir en leur valeur
        card = "Jack"
    elif card == 12:
        card = "Queen"
    elif card == 13:
        card = "King"
    elif card == 14:
        card = "Ace"
    #on ajoute les cartes à la main
    main.append(card)
    # main.append(symbole.pop())

"""
- Cette fonction vérifie si la valeur de la main (des 2 prmières cartes) du joueur est de 21. 
Si cela est le cas alors la fonction blackjack renvoie 1 sinon elle renvoie 0. Cette valeur sera 
sauvergardé dans une variable pour ensuite évaluer la situation dans le fichier 'game.py'.

- Cette fonction a comme arguments la valeur de la main, car forcément si les premières 2 cartes ont une 
valeurde 21, la main aura un As et une image ou un 10 donc il n y est pas besoin de connaitre la main du joueur.
"""


def blackjack(value):
    if value == 21:
        return 1
    else:
        return 0


"""
- Cette fonction 'split' la main du joueur et jouera pour celles 2 parties, elle renvoie ensuite
la première main avec la valeur et la deuxième avec la valeur. 

- Cette fonction a comme arguments la main du joueur et sa valeur.
"""

#NOTICE: Il reste a implémenter le tirage des cartes dans le game.py


def split(main_joueur):
    for _ in range(2):
        main_joueur.append(deck.pop())
    
    return main_joueur


"""
- Cette fonction compare simplement les valeurs du dealer et du joueur et
détermine ensuite le résultat adapté a la fonction bet() qui déterminera
l´argent gagné par le joueur. 

- Cette fonction a comme arguments la valeur du dealer et celle du joueur. 
"""


def comparaison(dealer_value, player_value):
    # La variable 'result' sera ensuite interpreter par la fonction 'bet()'
    if dealer_value == player_value:
        result = "draw"
    elif player_value > dealer_value:
        result = "gagne"
    else:
        result = "perdu"
    return result


"""
- Cette fonction calculera en fonction de la variable 'resultat' le montant
brut gagné du joueur, elle le renvoie ensuite. Cette valeur sera ensuite sauvegardé
dans une variable pour qu´elle soit ajouté à la banque du joueur (fichier 'menu.py').

- Cette fonction a comme arguments le resultat de la comparaison et la mise du joueur.
"""


def bet(resultat1, bet=0):
    # La variable 'result' a été définie avant par la fonction 'comparaison()'
    if resultat1 == "blackjack":
        # Montant brute qui sera ajouté à la banque du joueur
        bonus = 1.5 * bet
        bet *= 2
        bet += bonus
    elif resultat1 == "gagne":
        bet *= 2
    elif resultat1 == "draw":
        bet = bet
    elif resultat1 == "perdu":
        bet = 0

    return bet
