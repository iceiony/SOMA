# distutils: language = c++
import numpy as np
from decl cimport HelloWorld

def train(data, dim):
    try:
        hello_ptr = new HelloWorld()
    finally:
        del hello_ptr;

    if len(dim) == 1:
        dim.append(1)

    dim = np.append(dim, data.shape[1:])

    out = (np.repeat(0, np.prod(dim))
             .reshape(dim))

    return out

def plot(feature_map):
    pass

