# **Projet de blackjack pour la fin de l'année (American Blackjack)**.

<br><br>

# **Structure détaillée du projet (partie simulation / data-science):**.

<br>

## 2 - [ ] Simuler et collecter des données et les travailler/interpréter (statistiques, comptage, combinatoire) (deuxième partie la plus difficile & haute priorité) sur la branche data / branche mathématique.

    2.1 - [x] Automatiser les flux de jeu

        2.1.1 - [x] Créer la classe 'Simulation'

        2.1.2 - [x] Protocoller les résultats (boucle while) : pour prendre automatiquement des cartes jusqu'à n points

        2.1.3 - [x] Protocoller les résultats (boucle while) : pour doubler automatiquement les cartes.

        2.1.4 - [x] Protocoller les Blackjacks (pour le groupier et le(s) joueur(s))

        2.1.5 - [x] Protocoller les nombres de gains/pertes

        2.1.6 - [x] Protocoller la raison du gain/de la perte (bj, surachat, comparaison)

        2.1.7 - [x] Protocoller l'efficacité du temps pour toutes ces opérations.


    2.2 - [ ] Collecter toutes les formules et outils mathématiques

        2.2.1 - [x] Les écrire dans des fonctions ou des Classes dans Math.py
        2.2.2 - [ ] Noter pour chaque cas/opération celle à utiliser

    2.3 - [ ] Comptage des cartes (croupier et joueur(s))

        2.3.1 - [ ] Combien de chiffres/figures sur n cartes ? (voir 2.3)
        2.3.2 - [ ] Quelles couleurs et figures parmi ces n images ? (voir 2.3)


    2.4 - [ ] Protocoller le nombre de n parties gagnées/perdues

            2.4.1 - [x] Combien de parties gagnées/perdues sur les n parties totales ? (groupier et joueur(s))

            2.4.2 - [ ] Combien de parties consécutives gagnées/perdues sur n parties totales ? (groupier et joueur(s))

                2.4.2.1 - [ ] Utiliser un ABR pour le représenter (en ignorant les égalitées)

                    2.4.2.1.1 - [ ] Implémenter une classe ABR (nœud)
                    2.4.2.1.2 - [ ] Insérer toutes les données pertinentes
                    2.4.2.1.3 - [ ] Enregistrer toutes les données consécutives pour n parties


    2.6 - [x] Faire le triangle pascal (éventuellement de manière récursive) pour décompter n types de cartes sur p cartes

        2.6.1 - [x] Choisir la structure de données (probablement une matrice 2d)
        2.6.2 - [x] Résoudre le problème récursivement ou itérativement avec un temps maximum de 0(n^2)

    2.7 - [ ] Probabilités (IMPORTANT)

    2.8 - [x] Choisir les structures de données à partir des outputs (ABR pour 2.4.2, ensemble, tableaux...)

        2.8.1 - [x] Ensemble (tableau d'ensembles pour la clé du jeu) pour les résultats bruts des simulations (2.1).

<br>

## 3 - [ ] Redresser les résultats/stats vers un fichier CSV (peut-être JSON) pour l'interprétation et la DB SQL (priorité moyenne).

    3.1 - [ ] Choisir la structure de données des exportations pour SQL

        3.1.1 - [x] JSON/CSV pour 2.7.1

    3.1 - [ ] Stocker les données dans des fichiers CSV/JSON (multiples ?)

        - [x] JSON (json.dump(data, file, indent=2) en mode écriture)

        - [ ] CSV

            - [ ] Définir des lignes d'en-tête (gameId, won, reason, cards, dealer_cards...)
            - [ ] Délimiteur
            - [ ] Écriture en CSV : (https://www.programiz.com/python-programming/writing-csv-files)

    3.2 - [ ] Exportation vers un fichier séparé et préparation des résultats pour SQL

        3.2.1 - [ ] Comment faire : https://www.sqlshack.com/importing-and-working-with-csv-files-in-sql-server/

<br>
