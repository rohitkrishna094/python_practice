import numpy as np
import matplotlib.pyplot as plt
from Perceptron import Perceptron


def generateInputs(numberOfPoints, line):
    '''
    numberOfPoints  : number of inputs you want
    line            : the function that represents the line
    '''
    arr = []
    for i in range(numberOfPoints):
        x1, y1 = np.random.random(), np.random.random()
        arr.append([x1, y1, 1 if y1 - line(x1) >= 0 else -1])

    arr = np.array(arr)
    return arr


arr = generateInputs(10, lambda x: 0.9 - 0.7 * x)
p = Perceptron(arr)
# print(Perceptron)

# plt.scatter(arr[:, 0], arr[:, 1], c=arr[:, 2], cmap="bwr_r")
# x = np.linspace(0, 1, 10)
# plt.axis([0, 1, 0, 1])
# plt.plot(x, (lambda x: 0.9 - 0.7 * x)(x))
# plt.show()
