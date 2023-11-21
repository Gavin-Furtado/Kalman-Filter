'''
This module is used as an example to implement Kalman filter
algorithm using FilterPy library.

Documentation: https://filterpy.readthedocs.io/en/latest/# 

GitHub: https://github.com/rlabbe/filterpy 

GitHub book: https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python/blob/master/00-Preface.ipynb 

PDF book: https://drive.google.com/file/d/0By_SW19c1BfhSVFzNHc0SjduNzg/view?resourcekey=0-41olC9ht9xE3wQe2zHZ45A 

Date: 15 November 2023
Author: Gavin Furtado
'''

# from filterpy.kalman import KalmanFilter
# from filterpy.common import Q_discrete_white_noise
# import numpy as np

# f = KalmanFilter(dim_x=2, dim_z=1)

# # State Matrix
# f.x = np.array([[2.],
#                 [0.]])

# # State Transistion Matrix
# f.F = np.array([[1.,1.],
#                 [0.,1.]])

# # Measurement function
# f.H = np.array([[1.,0.]])

# # Covariance matrix
# f.P = np.array([[1000.,0.],
#                 [0.,1000.]])

# # Measurement Noise 
# f.R = np.array([[5.]])

# # Discrete white noise
# f.Q = Q_discrete_white_noise(dim=2, dt=0.1, var=0.13)


from numpy.random import randn

class PosSensor(object):
    def __init__(self, pos=(0,0), vel=(0,0), noise_std=1.):
        self.vel = vel
        self.noise_std = noise_std
        self.pos = [pos[0],pos[1]]

    def read(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1] 

        return [self.pos[0] + randn() * self.noise_std,
                self.pos[1] + randn() * self.noise_std]