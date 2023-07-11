from similarity.use_case import similarity
from similarity.use_case.similarity import Similarity
from use_case.nominal import Nominal as Nom
from use_case.numeric import Numeric as Num
from use_case.ordinal import Ordinal as Ord


# Create your tests here.

def test_ordinal():
    # hasil = Ord([Ord.excellent(), Ord.fair(), Ord.good(), Ord.excellent(), Ord.fair(), Ord.good()])
    hasil = Ord(Ord.generator(100))
    print(str('MAX: ' + str(hasil.get_max())))
    print(str('MIN: ' + str(hasil.get_min())))
    print(str('DATA: ' + str(hasil.get_data())))
    print(str('PRE-NORMALISASI: ' + str(hasil.get_pre_normalisasi())))
    print(str('NORMALISASI: ' + str(hasil.get_normalisasi())))
    print(str('' + str(hasil.get_matrix(True))))
    return hasil


def test_nominal():
    hasil = Nom(['B', 'D', 'A', 'B', 'B', 'C'])
    print(str('DATA: ' + str(hasil.get_data())))
    print(str('' + str(hasil.get_matrix(True))))
    return hasil


def test_numeric():
    hasil = Num([80, 50, 90, 75, 82, 65])
    print(str('MAX: ' + str(hasil.get_max())))
    print(str('MIN: ' + str(hasil.get_min())))
    print(str('DATA: ' + str(hasil.get_data())))
    print(str('NORMALISASI: ' + str(hasil.get_normalisasi())))
    print(str('' + str(hasil.get_matrix(True))))
    return hasil


def test_similarity():
    hasil = Similarity()
    print(hasil.get_matrix())
    return hasil.get_matrix()


if __name__ == '__main__':
    # print(Ord.generator(10))

    # test_ordinal()
    # test_nominal()
    test_numeric()
    # test_similarity()



