# neural network for the blackjack game
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils.generic_utils import *

class Model:
    def __init__(self, epochs):
        # creating the nn model for later
        self.model = Sequential() 
        # 5 layers of neurons for this one
        self.layers = [16, 128, 32, 8] 
        # last layer for activation (1)
        self.activation = "sigmoid" # this function converts raw output to readable ouput
        self.loss = "binary_crossentropy" # good for outputting probabilities
        self.optimizer = "sgd"
        self.epochs = epochs
        self.batch_size = 256
        self.verbose = 1

    def setup(self, train_x, train_y): 
        # adding the 5 neural layers
        for layer in self.layers: # not the last one
            self.model.add(Dense(layer))
        # active the last layer with a activation function
        self.model.add(Dense(1, activation=self.activation))
        # compiling with a probability adapted method/optimization
        self.model.compile(loss=self.loss, optimizer=self.optimizer)
        self.model.fit(train_x, train_y, epochs=self.epochs, batch_size=self.batch_size, verbose=self.verbose)
        self.prediction_results = self.model.predict(train_x)
        self.loss_results = train_y[:, -1]
        # print(self.loss_results)
    
    # method which lets the nn make a prediction and then decides to either hit or stay
    def prediction(self, player_sum, has_ace, dealer_card_val, coeff=0.52):
        # making the prediction
        self.input_array = np.array([player_sum, 0, has_ace, dealer_card_val]).reshape(1, -1)
        self.correct_predict = self.model.predict(self.input_array)
        # deciding to hit or not
        if (self.correct_predict >= coeff): # more likely to stay to avoid bust (>= 0.5)
            return 1
        else:
            return 0
