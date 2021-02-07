# **Blackjack project for the end of the year (American Blackjack)**

<br><br>

# **Detailed structure of the project:**

<br>

## 1 - [ ] Rework the entire Codebase using classes, methods...

    1.1 - [ ] Remanaging file connection(s)


    1.2 - [ ] Restructure Algorithm

        1.2.1 - [ ] Start replacing functions by classes

            1.2.1.1 - [ ] StartingScreen Class (selecting overlay w/ different options)

            1.2.1.2 - [ ] Cards Class (+ tracking the decks/cards, hit/pass method...)

            1.2.1.2 - [ ] Game Class (split method, double method)

        1.2.2 - [ ] Remanage gameflow

            1.2.2.1 - [ ] Relook the precise rules

            1.2.2.2 - [ ] Adapt gameflow/conditions

        1.2.3 - [ ] Adding the possibility to play with multiple people


    1.3 - [ ] Automating gameflows for future data gathering

        1.3.1 - [ ] Protocolling Condition (while loop): for taking automaticly cards up to n points

        1.3.2 - [ ] Protocolling Blackjacks (for dealer and player(s))

        1.3.3 - [ ] Protoclling the reason of win/lost (bj, overbought, point-win)

        1.3.4 - [ ] Decounting/protocolling of cards (dealer and player(s))

            1.3.4.1 - [ ] How much numbers/pictures out of the n number of cards ?
            1.3.4.2 - [ ] Which colors & figures out of these n pictures ?


    1.4 - [ ] Debugging & Error handeling

        1.4.1 - [ ] Hardcoding all possible outcomes
        1.4.2 - [ ] Rework the conditional error handeling

<br>

## 2 - [ ] Simulating/gathering data and work/interpretate them (statistics, count, combinatorics) (second hardest part)

<br>

## 3 - [ ] Righting the results/stats to a CSV file for interpretation and SQL (later)

<br>

## 4 - [ ] Implement CSV results in a SQL Database (MySQL probably) (third hardest part)

    3.1 - [ ] Define/Create DB Diagramm in MySQL Workbench

        3.1.1 - [ ] Create brieve Structure
        3.1.2 - [ ] Model Tables
        3.1.3 - [ ] Model attributes
        3.1.4 - [ ] Relation between tables / PK´s & FK´s


    3.2 - [ ] Write/Create SQL script (sqlshack.com/importing-and-working-with-csv-files-in-sql-server/)
        3.2.1 - [ ] Starting with Tables/attributes

    3.3 - [ ] Connect to DB

## 5 - [ ] Load & preprocess data for neural network w/ TensorFlow (hardest part)

    4.1 - [ ] Install (locally) all libraries & modules w/ pip

        4.1.1 - [ ] Install [TensorFlow](https://www.tensorflow.org/install/pip)
        4.1.2 - [ ] Install matplotlib: python -m pip install -U matplotlib
        4.1.4 - [ ] Install pandas: pip intall pandas
        4.1.4 - [ ] Install matplotlib: pip install numpy


    4.2 - [ ] Learn basic mecanics


    4.4 - [ ] Read input data (probably from generated CSV file)

        4.4.1 - [ ] Consume CSV file (probably)
        4.4.2 - [ ] Prepare for preprocessing


    4.4 - [ ] Training workflows (maybe optional)

        4.4.1 - [ ] Processing multiple epochs (less interesting, repeating events, visualisation)

        4.4.2 - [ ] Randomly shuffling input data (quite interesting for comparing randomized behavior)

            4.4.2.1 - [ ] Finding a way to compare random games --> search for pattern/function
            4.4.2.2 - [ ] Interpretate mathematical behavior/attributes


    4.5 - [ ] Preprocessing CSV data (if needed)


    4.6 - [ ] Resampling data / check if it´s skewed and representative (low priority)


    4.7 - [ ] Iterator Checkpointig / storing latest data during multiple training process

<br>

## 6 - [ ] Visualizing results (low priority)
