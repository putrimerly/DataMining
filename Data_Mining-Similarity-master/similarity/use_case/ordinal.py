import numpy as np
from matplotlib import pyplot as plt


class Ordinal:

    @staticmethod
    def excellent():
        return 'excellent'

    @staticmethod
    def good():
        return 'good'

    @staticmethod
    def fair():
        return 'fair'

    @staticmethod
    def generator(count=5):
        result = []
        for i in range(count):
            random = np.random.randint(1, 3)
            if random == 1:
                result.append(Ordinal.excellent())
            elif random == 2:
                result.append(Ordinal.good())
            elif random == 3:
                result.append(Ordinal.fair())
        return result

    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def get_pre_normalisasi(self):
        result = []
        for i in self.data:
            if i == self.excellent():
                result.append(3)
            elif i == self.fair():
                result.append(2)
            elif i == self.good():
                result.append(1)
        return result

    def get_normalisasi(self):
        result = []
        for i in self.get_pre_normalisasi():
            result.append((i - self.get_min()) / (self.get_max() - self.get_min()))
        return result

    def get_matrix(self, isMatrix=True):
        result = []
        for i in self.get_normalisasi():
            value = []
            for j in self.get_normalisasi():
                if j == i:
                    value.append(0)
                else:
                    value.append(np.around(np.sqrt(np.power(j - i, 2)), decimals=2))
            result.append(value)

        if isMatrix:
            return np.matrix(result)

        return result

    def get_max(self):
        return max(self.get_pre_normalisasi())

    def get_min(self):
        return min(self.get_pre_normalisasi())

    def get_image(self, title='Similarity Matrix Ordinal'):
        matrix = self.get_matrix()

        plt.clf()
        plt.imshow(matrix, cmap='hot', interpolation='nearest')
        plt.colorbar()
        plt.title(title)
        plt.xticks(np.arange(len(matrix)), np.arange(1, len(matrix) + 1))
        plt.yticks(np.arange(len(matrix)), np.arange(1, len(matrix) + 1))
        # plt.show()

        temp_file = 'static/assets/img/plot/plot-ordinal.png'
        plt.savefig(temp_file)
        return temp_file
