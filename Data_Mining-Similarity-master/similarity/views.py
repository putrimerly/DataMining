import numpy as np
from django.shortcuts import render

from similarity.use_case.nominal import Nominal
from similarity.use_case.numeric import Numeric
from similarity.use_case.ordinal import Ordinal
from similarity.use_case.similarity import Similarity

v_numeric = [80, 50, 90, 75, 82, 65]
v_ordinal = [Ordinal.excellent(), Ordinal.fair(), Ordinal.good(), Ordinal.excellent(), Ordinal.fair(), Ordinal.good()]
v_nominal = ['B', 'D', 'A', 'B', 'B', 'C']


def index(request):
    x = Similarity()
    data = np.transpose(np.array([v_ordinal, v_numeric, v_nominal]))
    matrix = x.get_matrix()

    ord = Ordinal(v_ordinal)
    test1 = ord.get_image()

    num = Numeric(v_numeric)
    test2 = num.get_image()

    nom = Nominal(v_nominal)
    test3 = nom.get_image()

    sim = Similarity()
    test4 = sim.get_image()

    akhir = sim.get_matrix(v_numeric, v_ordinal, v_nominal)
    kumpulan = {
        'nominal': nom.get_matrix(False),
        'numeric': num.get_matrix(False),
        'ordinal': ord.get_matrix(False),
        'similarity': akhir,
    }
    temp_file = x.get_image_x(kumpulan)

    return render(request, 'index.html', {
        'id': 0,
        'data': data,
        'v_numeric': v_numeric,
        'v_ordinal': v_ordinal,
        'v_nominal': v_nominal,
        'matrix': matrix,
        'plot_image': temp_file,
        'test1': test1,
        'test2': test2,
        'test3': test3,
        'test4': test4,
    })


def numeric(request):
    numberic = Numeric(v_numeric)
    data = np.transpose(np.array([v_ordinal, v_numeric, v_nominal]))
    normalisasi = numberic.get_normalisasi()
    matrix = numberic.get_matrix(False)
    v_min = numberic.get_min()
    v_max = numberic.get_max()
    temp_file = numberic.get_image()

    return render(request, 'index.html', {
        'id': 2,
        'data': data,
        'v_numeric': v_numeric,
        'v_ordinal': v_ordinal,
        'v_nominal': v_nominal,
        'numberic': numberic,
        'normalisasi': normalisasi,
        'matrix': matrix,
        'v_min': v_min,
        'v_max': v_max,
        'plot_image': temp_file
    })


def nominal(request):
    x = Nominal(v_nominal)
    data = np.transpose(np.array([v_ordinal, v_numeric, v_nominal]))
    normalisasi = x.get_normalisasi()
    matrix = x.get_matrix(False)
    v_min = x.get_min()
    v_max = x.get_max()
    temp_file = x.get_image()

    return render(request, 'index.html', {
        'id': 3,
        'data': data,
        'v_numeric': v_numeric,
        'v_ordinal': v_ordinal,
        'v_nominal': v_nominal,
        'numberic': x,
        'normalisasi': normalisasi,
        'matrix': matrix,
        'v_min': v_min,
        'v_max': v_max,
        'plot_image': temp_file
    })


def ordinal(request):
    x = Ordinal(v_ordinal)
    data = np.transpose(np.array([v_ordinal, v_numeric, v_nominal]))
    normalisasi = x.get_normalisasi()
    matrix = x.get_matrix(False)
    v_min = x.get_min()
    v_max = x.get_max()
    temp_file = x.get_image()

    return render(request, 'index.html', {
        'id': 1,
        'data': data,
        'v_numeric': v_numeric,
        'v_ordinal': v_ordinal,
        'v_nominal': v_nominal,
        'numberic': x,
        'normalisasi': normalisasi,
        'matrix': matrix,
        'v_min': v_min,
        'v_max': v_max,
        'plot_image': temp_file
    })
