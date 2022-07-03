from numpy import array, zeros, argmin, inf, equal, ndim
from scipy.spatial.distance import cdist
from MFCC import mfcc
from numpy.linalg import norm
import scipy.io.wavfile as wav
import json
import numpy as np


def dtw(x, y, dist):
    assert len(x)  # Report error while x is none
    assert len(y)
    r, c = len(x), len(y)
    D0 = zeros((r + 1, c + 1))
    D0[0, 1:] = inf
    D0[1:, 0] = inf
    D1 = D0[1:, 1:]  # view

    for i in range(r):
        for j in range(c):
            D1[i, j] = dist(x[i], y[j])
    C = D1.copy()

    for i in range(r):
        for j in range(c):
            D1[i, j] += min(D0[i, j], D0[i, j + 1], D0[i + 1, j])
    if len(x) == 1:
        path = zeros(len(y)), range(len(y))
    elif len(y) == 1:
        path = range(len(x)), zeros(len(x))
    else:
        path = _traceback(D0)
    return D1[-1, -1] / sum(D1.shape), C, D1, path


def _traceback(D):
    i, j = array(D.shape) - 2
    p, q = [i], [j]
    while ((i > 0) or (j > 0)):
        tb = argmin((D[i, j], D[i, j + 1], D[i + 1, j]))
        if (tb == 0):
            i -= 1
            j -= 1
        elif (tb == 1):
            i -= 1
        else:  # (tb == 2):
            j -= 1
        p.insert(0, i)
        q.insert(0, j)
    return array(p), array(q)


def calcDTW(filename):
    (rate_test, sig_test) = wav.read(r"{0}".format(filename))
    # read words
    with open("data_file.json", "r") as read_file:
        data = json.load(read_file)

    # calc mfcc
    mfcc_test = mfcc(signal=sig_test, samplerate=rate_test)

    with open('words.txt', 'r') as words_list:
        lines = words_list.read().splitlines()
    distances = dict.fromkeys(lines)

    for word in lines:
        dist, cost, acc, path = dtw(data[word], mfcc_test, dist=lambda x, y: norm(x - y, ord=1))
        distances[word] = dist
    word = min(distances, key=distances.get)
    dist_test, cost_test, acc_test, path_test = dtw(data[word], mfcc_test, dist=lambda x, y: norm(x - y, ord=1))
    result_test = np.zeros((len(data[word]), 13))
    for x in range(path_test[0].size-1):
        result_test[path_test[0][x], :] = mfcc_test[x, :]
    return(result_test, word)

