import numpy as np
from matplotlib import pyplot as plt


class Nominal:

    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def get_normalisasi(self):
        result = []
        for i in self.data:
            value = []
            for j in self.data:
                if j == i:
                    value.append(0)
                else:
                    value.append(1)
            result.append(value)

        return result[0]

    def get_matrix(self, isMatrix=True):
        result = []
        for i in self.data:
            value = []
            for j in self.data:
                if j == i:
                    value.append(0)
                else:
                    value.append(1)
            result.append(value)

        if isMatrix:
            return np.matrix(result)

        return result

    def get_max(self):
        return max(self.data)

    def get_min(self):
        return min(self.data)

    def get_image(self, title='Similarity Matrix Nominal'):
        matrix = self.get_matrix()

        plt.clf()
        plt.imshow(matrix, cmap='hot', interpolation='nearest')
        plt.colorbar()
        plt.title(title)
        plt.xticks(np.arange(len(matrix)), np.arange(1, len(matrix) + 1))
        plt.yticks(np.arange(len(matrix)), np.arange(1, len(matrix) + 1))
        # plt.show()

        temp_file = 'static/assets/img/plot/plot-nominal.png'
        plt.savefig(temp_file)
        return temp_file
