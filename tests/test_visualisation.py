import numpy as np
import soma

def test_can_visualise_1d_data():
    feature_map = np.array([[0, 0, 1],
                            [0, 1, 1]]).reshape(2, 1, -1)
    soma.plot(feature_map)

def test_can_visualise_2d_data():
    feature_map = np.array([[0, 0, 1],[0, 0, 0],
                            [0, 1, 1],[1, 1, 0]]).reshape(2, 2, -1)
    soma.plot(feature_map)

def test_can_visualise_3d_data():
    feature_map = np.array([ [0,0,1],[0,0,0],
                             [0,1,1],[1,1,0],

                             [1,0,0],[1,1,1],
                             [1,0,1],[0,1,0] ]).reshape(2,2,2, -1)

    soma.plot(feature_map)

