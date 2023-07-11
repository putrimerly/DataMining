import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import TSNE

from similarity.use_case.nominal import Nominal
from similarity.use_case.numeric import Numeric
from similarity.use_case.ordinal import Ordinal


class Similarity:

    def get_matrix(self, array_numeric=None, array_ordinal=None, array_nominal=None):
        if array_nominal is None:
            array_nominal = ['B', 'D', 'A', 'B', 'B', 'C']
        if array_numeric is None:
            array_numeric = [80, 50, 90, 75, 82, 65]
        if array_ordinal is None:
            array_ordinal = [Ordinal.excellent(), Ordinal.fair(), Ordinal.good(), Ordinal.excellent(),
                             Ordinal.fair(), Ordinal.good()]
        c_numeric = Numeric(array_numeric)
        c_ordinal = Ordinal(array_ordinal)
        c_nominal = Nominal(array_nominal)

        matrix_numeric = np.array(c_numeric.get_matrix(False))
        matrix_ordinal = np.array(c_ordinal.get_matrix(False))
        matrix_nominal = np.array(c_nominal.get_matrix(False))

        # print(matrix_numeric)
        # print(matrix_ordinal)
        # print(matrix_nominal)

        return np.around((matrix_numeric + matrix_ordinal + matrix_nominal) / 3, decimals=2)

    def get_image(self, title='Similarity Matrix Visualization'):
        matrix = self.get_matrix()

        plt.clf()
        plt.imshow(matrix, cmap='hot', interpolation='nearest')
        plt.colorbar()
        plt.title(title)
        plt.xticks(np.arange(len(matrix)), np.arange(1, len(matrix) + 1))
        plt.yticks(np.arange(len(matrix)), np.arange(1, len(matrix) + 1))
        # plt.show()

        temp_file = 'static/assets/img/plot/plot-similarity.png'
        plt.savefig(temp_file)
        return temp_file

    def get_image_x(self, data):
        # Contoh data similarity
        nominal_data = np.array(data['nominal'])
        numeric_data = np.array(data['numeric'])
        ordinal_data = np.array(data['ordinal'])
        similarity_data = np.array(data['similarity'])

        tsne = TSNE(n_components=3, perplexity=5, learning_rate=2, n_iter=2000, random_state=4)

        nominal_embedding = tsne.fit_transform(nominal_data)
        numeric_embedding = tsne.fit_transform(numeric_data)
        ordinal_embedding = tsne.fit_transform(ordinal_data)
        similarity_embedding = tsne.fit_transform(similarity_data)

        plt.clf()

        plt.scatter(nominal_embedding[:, 0], nominal_embedding[:, 1], c='red', label='Nominal')
        plt.scatter(numeric_embedding[:, 0], numeric_embedding[:, 1], c='blue', label='Numeric')
        plt.scatter(ordinal_embedding[:, 0], ordinal_embedding[:, 1], c='yellow', label='Ordinal')
        plt.scatter(similarity_embedding[:, 0], similarity_embedding[:, 1], c='black', label='Similarity')

        plt.title('Similarity Visualization (t-SNE)')
        plt.xlabel('Dimensi 1')
        plt.ylabel('Dimensi 2')
        plt.legend()
        # plt.show()

        temp_file = 'static/assets/img/plot/plot-finali.png'
        plt.savefig(temp_file)
        return temp_file

