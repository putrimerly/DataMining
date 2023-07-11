import os

import numpy as np
from matplotlib import pyplot as plt


class Numeric:

    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def get_normalisasi(self):
        result = []
        for i in self.data:
            result.append(abs((i - self.get_min()) / (self.get_max() - self.get_min())))
        return result

    def get_matrix(self, isMatrix=True):
        result = []
        for i in self.get_normalisasi():
            value = []
            for j in self.get_normalisasi():
                if j == i:
                    value.append(0)
                else:
                    value.append(np.around(abs(i - j), decimals=2))
            result.append(value)

        if isMatrix:
            return np.matrix(result)

        return result

    def get_max(self):
        return max(self.data)

    def get_min(self):
        return min(self.data)

    def get_image(self,title='Similarity Matrix Numeric'):
        matrix = self.get_matrix()

        plt.clf()
        plt.imshow(matrix, cmap='hot', interpolation='nearest')
        plt.colorbar()
        plt.title(title)
        plt.xticks(np.arange(len(matrix)), np.arange(1, len(matrix) + 1))
        plt.yticks(np.arange(len(matrix)), np.arange(1, len(matrix) + 1))
        # plt.show()

        temp_file = 'static/assets/img/plot/plot-numeric.png'
        plt.savefig(temp_file)
        return temp_file
