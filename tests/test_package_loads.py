import numpy as np


def test_library_loads_correctly():
    """library loads with no error"""
    import soma

def test_trains_on_dataset():
    """trains unsupervised on a dataset in finit time"""
    import soma

    data = np.array([
    [0,0,0],
    [1,1,1],
    ])

    feature_map = soma.train(data, dim = [2])

    assert(feature_map is not None)
    assert(type(feature_map) is np.ndarray)

    assert(feature_map.shape == (2, 1, 3))

    assert( (feature_map == np.array([[0, 0, 0], [1, 1, 1]])).all() )
