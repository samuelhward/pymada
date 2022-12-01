import pymada.errors

import numpy as np


class Layer:
    """neural net layer"""

    def __init__(self, number_neurons):

        self.number_neurons = number_neurons
        self.neurons = np.zeros(self.number_neurons)
