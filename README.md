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

            1.2.1.3 - [ ] Game Class (split method, double method)

            1.2.1.4 - [ ] StartingScreen Class (choice, checkout, gameFlow)

        1.2.2 - [x] Remanage gameflow (medium-priority)

            1.2.2.1 - [x] Relook the precise rules

            1.2.2.2 - [x] Adapt gameflow/conditions

        1.2.3 - [ ] Adding the possibility to play with multiple people (low-priority)

            1.2.3.1 - [x] Pseudo-alternatives written

    1.3 - [ ] Automating/protoclling gameflows for future data gathering

        1.3.1 - [ ] Protocolling Condition (while loop): for taking automaticly cards up to n points

        1.3.2 - [ ] Protocolling Blackjacks (for dealer and player(s))

        1.3.3 - [ ] Protoclling the reason of win/lost (bj, overbought, point-win)


    1.4 - [ ] Debugging & Error handeling

        1.4.1 - [ ] Hardcoding all possible outcomes
        1.4.2 - [ ] Rework the conditional error handeling

<br>

## 2 - [ ] Simulating/gathering data and work/interpretate them (statistics, count, combinatorics) (second hardest part & high priority) on data branch / math branch

    2.1 - [ ] Gathering statistics

        2.1.1 - [ ] Calculate percentages of 1.3 numbers


    2.2 - [ ] Collect all formulas and mathematical tools

        2.2.1 - [ ] Write them down in functions or Classes in formula.py
        2.2.2 - [ ] Note for each case/operation which one to use

    2.3 - [ ] Decounting/protocolling of cards (dealer and player(s))

        2.3.1. - [ ] How much numbers/pictures out of the n number of cards ? (goto 2.4)
        2.3.1. - [ ] Which colors & figures out of these n pictures ? (goto 2.4)


    2.4 - [ ] Protocolling number of n won/lost games

            2.4.1 - [ ] How much games lost/won out of n total games ? (dealer and player(s))

            2.4.2 - [ ] How much consecutive games lost/won out of n total games ? (dealer and player(s))

                2.4.2.1 - [ ] Use a BST for representing it

                    2.4.2.1.1 - [ ] Implement BST Class (Node)
                    2.4.2.1.2 - [ ] Inserting all relevant data
                    2.4.2.1.3 - [ ] Log all consecutive data for n games ((w, l, w) --> 4)


    2.5 - [ ] Do the pascale triangle (maybe recursively) for decounting n type of a card out ouf p cards

        2.5.1 - [ ] Choose data structure (probably 2d matrix)
        2.5.2 - [ ] Solve it recursively or iterative with 0(n^2) time max


    2.6 - [ ] Choose data structure from output (BT for 2.4.2, set, arrays...)

<br>
