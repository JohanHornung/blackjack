# neural network for the blackjack game
from keras.models import Sequential
from keras.layers import Dense


class Model:
    def __init__(self):
        # creating the nn model for later
        self.model = Sequential() 
        # 5 layers of neurons for this one
        self.layers = [16, 128, 32, 8, 1] 
        # last layer for activation (1)
        self.activation = "sigmoid" # this function converts raw output to readable ouput
        self.loss = "binary_crossentropy" # good for outputting probabilities
        self.optimizer = "sgd"
        self.epochs = 20
        self.batch_size = 256
        self.verbose = 1

    def setup(self, df_model, train_x, train_y):
        # adding the 5 neural layers
        for layer in self.layers[:-1]: # not the last one
            self.model.add(Dense(layer))
        # active the last layer with a activation function
        self.model.add(Dense(1, activation=self.activation))
        # compiling with a probability adapted method/optimization
        self.model.compile(loss=self.loss, optimizer=self.optimizer)
        self.model.fit(train_x, train_y, epochs=self.epochs, batch_size=self.batch_size, verbose=self.verbose)
        self.prediction = self.model.predict(train_x)
        self.loss_results = self.prediction[:, -1]
    
    # a way to evaluate the efficiency of the nn results
    def eval_roc(self):
        pass