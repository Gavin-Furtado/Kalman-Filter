'''
This module is used as an example to implement Kalman filter
algorithm using FilterPy library.

Documentation: https://filterpy.readthedocs.io/en/latest/# 

GitHub: https://github.com/rlabbe/filterpy 

GitHub book: https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python/blob/master/00-Preface.ipynb 

Date: 15 November 2023
Author: Gavin Furtado
'''

from filterpy.kalman import KalmanFilter
from filterpy.common import Q_discrete_white_noise
import numpy as np

f = KalmanFilter(dim_x=2, dim_z=1)

# State Matrix
f.x = np.array([[2.],
                [0.]])

# State Transistion Matrix
f.F = np.array([[1.,1.],
                [0.,1.]])

# Measurement function
f.H = np.array([[1.,0.]])

# Covariance matrix
f.P = np.array([[1000.,0.],
                [0.,1000.]])

# Measurement Noise 
f.R = np.array([[5.]])

# Discrete white noise
f.Q = Q_discrete_white_noise(dim=2, dt=0.1, var=0.13)

## Measurements ##
measurement_position = [4260, 4450, 4720, 5110, 5320, 5293, 5894, 5721]
measurement_velocity = [282, 285, 286, 290, 285, 293, 298, 297]


