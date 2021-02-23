# **Blackjack project for the end of the year (American Blackjack)**

<br><br>

# **Detailed structure of the project:**

<br>

## 1 - [ ] Rework the entire Codebase using classes, methods... (high priority) on codebase branch

    1.1 - [x] Remanaging file connection(s)

        1.1.1 - [x] Imports
        1.1.2 - [x] Avoid "vise versa" calls

    1.2 - [ ] Restructure Algorithm

        1.2.1 - [ ] Start replacing functions by classes

            1.2.1.1 - [x] Create config/tools file

            1.2.1.2 - [x] Deck Class (+ tracking the decks/cards/points, hit/double method...) (current version: 1.2)

            1.2.1.3 - [x] Game Class (split method, double method) (current version: 1.0)

            1.2.1.4 - [ ] StartingScreen Class (choice, checkout, gameFlow)

        1.2.2 - [x] Remanage gameflow (medium-priority)

            1.2.2.1 - [x] Relook the precise rules

            1.2.2.2 - [x] Adapt gameflow/conditions

        1.2.3 - [ ] Adding the possibility to play with multiple people (low-priority)

            1.2.3.1 - [x] Pseudo-alternatives written



    1.4 - [ ] Debugging & Error handeling

        1.4.1 - [ ] Hardcoding all possible outcomes (split is missing)
        1.4.2 - [ ] Rework the conditional error handeling (split is missing)

<br>

## 2 - [ ] Simulating/gathering data and work/interpretate them (statistics, count, combinatorics) (second hardest part & high priority) on data branch / math branch

    2.1 - [ ] Automating/protoclling gameflows

        2.1.1 - [ ] Simulation class (in progress)

        2.1.2 - [x] Protocolling Results (while loop): for taking automaticly cards up to n points

        2.1.3 - [ ] Protocolling Results (while loop): for automatically double down cards

        2.1.4 - [x] Protocolling Blackjacks (for dealer and player(s))

        2.1.5 - [x] Protoclling the reason of win/lost (bj, overbought, point-win)

    2.2 - [ ] Gathering statistics

        2.2.1 - [ ] Calculate percentages of the results from 2.1


    2.3 - [ ] Collect all formulas and mathematical tools

        2.3.1 - [ ] Write them down in functions or Classes in formula.py
        2.3.2 - [ ] Note for each case/operation which one to use

    2.4 - [ ] Decounting/protocolling of cards (dealer and player(s))

        2.4.1. - [ ] How much numbers/pictures out of the n number of cards ? (goto 2.4)
        2.4.1. - [ ] Which colors & figures out of these n pictures ? (goto 2.4)


    2.5 - [ ] Protocolling number of n won/lost games

            2.5.1 - [ ] How much games lost/won out of n total games ? (dealer and player(s))

            2.5.2 - [ ] How much consecutive games lost/won out of n total games ? (dealer and player(s))

                2.5.2.1 - [ ] Use a BST for representing it

                    2.5.2.1.1 - [ ] Implement BST Class (Node)
                    2.5.2.1.2 - [ ] Inserting all relevant data
                    2.5.2.1.3 - [ ] Log all consecutive data for n games ((w, l, w) --> 4)


    2.6 - [ ] Do the pascale triangle (maybe recursively) for decounting n type of a card out ouf p cards

        2.6.1 - [ ] Choose data structure (probably 2d matrix)
        2.6.2 - [ ] Solve it recursively or iterative with 0(n^2) time max


    2.7 - [ ] Choose data structures from outputs (BT for 2.4.2, set, arrays...)

        2.7.1 - [x] Array of dictionnaries for raw games results from simulations (2.1)

<br>
