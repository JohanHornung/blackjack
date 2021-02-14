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

            1.2.1.2 - [x] Deck Class (+ tracking the decks/cards/points, hit/double method...) (current version: 1.0)

            1.2.1.3 - [ ] Game Class (split method, double method)


        1.2.2 - [ ] Remanage gameflow (medium-priority)

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

## 3 - [ ] Righting the results/stats to a CSV (maybe JSON) file for interpretation and SQL (medium-priority) on data branch

    3.1 - [ ] Store data in (multiple?) CSV files

        3.1.1 - [ ] Define header-rows (gameId, won, reason, cards, dealer_cards...)
        3.1.2 - [ ] Delimiter
        3.1.3 - [ ] Writing to CSV: (https://www.programiz.com/python-programming/writing-csv-files)
            3.1.3.1 - [ ] Choose which data structure to use (will be already decided in 2.6)

    3.2 - [ ] Exporting to a seperate file and prepare results for SQL

        3.2.1 - [ ] How-to: https://www.sqlshack.com/importing-and-working-with-csv-files-in-sql-server/

<br>

## 4 - [ ] Implement CSV results in a SQL Database (MySQL probably) (third hardest part) (medium-priority) on db branch

    4.1 - [ ] Define/Create DB Diagramm in MySQL Workbench

        4.1.1 - [ ] Create brieve Structure
        4.1.2 - [ ] Model Tables
        4.1.3 - [ ] Model attributes
        4.1.4 - [ ] Relation between tables / PK´s & FK´s


    4.2 - [ ] Write/Create SQL script (sqlshack.com/importing-and-working-with-csv-files-in-sql-server/)

        4.2.1 - [ ] Starting with Tables/attributes

    4.3 - [ ] Connect to DB

## 5 - [ ] Load & preprocess data for neural network w/ TensorFlow (hardest part) (high-priority) on neural network branch

    5.1 - [ ] Install (locally) all libraries & modules w/ pip

        5.1.1 - [ ] Install TensorFlow: https://www.tensorflow.org/install/pip
        5.1.2 - [ ] Install matplotlib: python -m pip install -U matplotlib
        5.1.3 - [ ] Install pandas: pip intall pandas
        5.1.4 - [ ] Install matplotlib: pip install numpy


    5.2 - [ ] Learn basic mecanics

        5.2.1 - [ ] Basic modules/syntax
        5.2.2 - [ ] Basic data sets

    5.3 - [ ] Read input data (probably from generated CSV file)

        5.3.1 - [ ] Consume CSV file (probably)
        5.3.2 - [ ] Prepare for preprocessing


    5.4 - [ ] Training workflows (maybe optional) (medium-priority)

        5.4.1 - [ ] Processing multiple epochs (less interesting, repeating events, visualisation)

        5.4.2 - [ ] Randomly shuffling input data (quite interesting for comparing randomized behavior)

            5.4.2.1 - [ ] Finding a way to compare random games --> search for pattern/function
            5.4.2.2 - [ ] Interpretate mathematical behavior/attributes


    5.5 - [ ] Preprocessing CSV data (if needed)

        5.5.1 [ ] Time series windowing
        5.5.2 [ ] Using batch


    5.6 - [ ] Resampling data / check if it´s skewed and representative (low priority)


    5.7 - [ ] Iterator Checkpointig / storing latest data during multiple training process (medium priority)

<br>

## 6 - [ ] Visualizing results (low priority) on math or data branch, maybe create a new one

    6.1 - [ ] Charts

        6.1.1 - [ ] Bar charts
        6.1.2 - [ ] Pie charts
        6.1.3 - [ ] Pictograms

    6.2 - [ ] Graphs

        6.2.1 - [ ] Line Graphs
        6.2.2 - [ ] Spider Graphs

    6.3 - [ ] Evolutions
