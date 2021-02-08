# **Blackjack project for the end of the year (American Blackjack)**

<br><br>

# **Detailed structure of the project:**

<br>

## 1 - [ ] Rework the entire Codebase using classes, methods... (high priority)

    1.1 - [ ] Remanaging file connection(s)


    1.2 - [ ] Restructure Algorithm

        1.2.1 - [ ] Start replacing functions by classes

            1.2.1.1 - [ ] StartingScreen Class (selecting overlay w/ different options)

            1.2.1.2 - [ ] Cards Class (+ tracking the decks/cards, hit/pass method...)

            1.2.1.2 - [ ] Game Class (split method, double method)

        1.2.2 - [ ] Remanage gameflow

            1.2.2.1 - [ ] Relook the precise rules

            1.2.2.2 - [ ] Adapt gameflow/conditions

        1.2.3 - [ ] Adding the possibility to play with multiple people (low-medium priority)


    1.3 - [ ] Automating/protoclling gameflows for future data gathering

        1.3.1 - [ ] Protocolling Condition (while loop): for taking automaticly cards up to n points

        1.3.2 - [ ] Protocolling Blackjacks (for dealer and player(s))

        1.3.3 - [ ] Protoclling the reason of win/lost (bj, overbought, point-win)


    1.4 - [ ] Debugging & Error handeling

        1.4.1 - [ ] Hardcoding all possible outcomes
        1.4.2 - [ ] Rework the conditional error handeling

<br>

## 2 - [ ] Simulating/gathering data and work/interpretate them (statistics, count, combinatorics) (second hardest part & high priority)

    2.1 - [ ] Gathering statistics

        2.1.1 - [ ] Decounting/protocolling of cards (dealer and player(s))

            2.1.1.1 - [ ] How much numbers/pictures out of the n number of cards ?
            2.1.1.2 - [ ] Which colors & figures out of these n pictures ?

        2.1.2 - [ ] Protocolling number of n won/lost games

            2.1.2.1 - [ ] How much games lost/won out of n total games ? (dealer and player(s))
            2.1.2.2 - [ ] How much consecutive games lost/won out of n total games ? (dealer and player(s))

<br>

## 3 - [ ] Righting the results/stats to a CSV (maybe JSON) file for interpretation and SQL (medium-priority)

<br>

## 4 - [ ] Implement CSV results in a SQL Database (MySQL probably) (third hardest part) (high-priority)

    4.1 - [ ] Define/Create DB Diagramm in MySQL Workbench

        4.1.1 - [ ] Create brieve Structure
        4.1.2 - [ ] Model Tables
        4.1.3 - [ ] Model attributes
        4.1.4 - [ ] Relation between tables / PK´s & FK´s


    4.2 - [ ] Write/Create SQL script (sqlshack.com/importing-and-working-with-csv-files-in-sql-server/)

        4.2.1 - [ ] Starting with Tables/attributes

    4.3 - [ ] Connect to DB

## 5 - [ ] Load & preprocess data for neural network w/ TensorFlow (hardest part) (high-priority)

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

## 6 - [ ] Visualizing results (low priority)
