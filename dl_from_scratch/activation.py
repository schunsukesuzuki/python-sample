import numpy as np
import matplotlib.pylab as plt

class activation:

    def __init__(self, x1, x2, x3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        # self.x4 = x4


    def step_function(self, x1):
        self.x1 = x1
        return np.array(x1 > 0, dtype = np.int)

    def sigmoid(self, x2):
        self.x2 = x2
        return 1 / (1 + np.exp(-x2))

    def relu(self, x3):
        self.x3 = x3
        return np.maximum(0, x3)

    # def identity_function(self, x4):
    #     self.x4 = x4
    #     return x4

if __name__ == "__main__":

    x1 = np.arange(-5.0, 5.0, 0.1)
    x2 = np.arange(-5.0, 5.0, 0.1)
    x3 = np.arange(-5.0, 5.0, 0.1)

    activation = activation(x1, x2, x3)

    y1 = activation.step_function(x1)
    plt.plot(x1, y1)
    plt.ylim(-0.1, 1.1)
    #plt.show()

    y2 = activation.sigmoid(x2)
    plt.plot(x2, y2)
    plt.ylim(-0.1, 1.1)

    plt.show()