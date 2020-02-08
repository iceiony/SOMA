# distutils: language = c++

import numpy as np
cimport soma

def train(data, dim):
    if len(dim) == 1:
        dim.append(1)

    dim = np.append(dim, data.shape[1:])

    out = (np.repeat(0, np.prod(dim))
             .reshape(dim))

    return out

def plot(feature_map):
    pass

