import numpy as np


class Perceptron():
    def __init__(self, inputs, epochs=200):
        self.weights = np.array([1, np.random.random(), np.random.random()])
        self.inputs = np.insert(inputs, 0, np.array([[1, 1, 1]]), 0)
        print(self.weights)
        print(self.inputs[:, :2])
        self.epochs = epochs

    def train(self):
        # for i in range(self.epochs):
        #     pass
        pass

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
