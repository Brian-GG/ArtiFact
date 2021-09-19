import random as ra

import numpy as np
import GetSetValues as gs


class Layer_Dense:
    def __init__(self, numofinputs, numofneurons):
        self.weights = gs.getWeightValues(numofinputs, numofneurons)
        self.biases = gs.getBiasValues(numofneurons)
        self.output = []

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


class Activation_ReLU:
    def __init__(self):
        self.output = []

    def forward(self, inputs):
        self.output = np.maximum(0, inputs)


class Activation_Softmax:
    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities


class Loss:
    def calculate(self, output, y):
        sample_losses = self.forward(output, y)
        data_loss = np.mean(sample_losses)
        return data_loss


def Identifier(check, num):
    return None


class PrintResult:
    def __init__(self):
        pass

    def printStatement(self, output):
        print("Result: ", output)


class Loss_Squared_Difference(Loss):
    def forward(self, y_pred, y_true):
        samples = len(y_pred)
        y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7)

        for i in range(y_pred_clipped):
            difference_of_squares = (y_pred_clipped - y_true) ** 2
        return difference_of_squares


def Get_ArtiFact_Score(X):
    layer_dense1 = Layer_Dense(40, 40)
    layer_activation1 = Activation_ReLU()
    layer_dense2 = Layer_Dense(40, 40)
    layer_activation2 = Activation_ReLU()
    layer_dense3 = Layer_Dense(40, 40)
    layer_activation3 = Activation_ReLU()
    checked = Identifier(X, layer_activation3.output)
    # Wonder if this will be read
    layer_dense4 = Layer_Dense(30, 1)
    layer_activation4 = Activation_Softmax()
    return checked
