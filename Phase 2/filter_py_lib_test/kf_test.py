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
import matplotlib.pyplot as plt
import numpy as np
from filterpy.kalman import KalmanFilter
from scipy.linalg import block_diag
from filterpy.common import Q_discrete_white_noise
from filterpy.stats import plot_covariance_ellipse

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
    
pos,vel =(4,3), (2,1)
sensor = PosSensor(pos, vel, noise_std=1)
ps = np.array([sensor.read() for _ in range(50)])
# plt.scatter(ps[:,0], ps[:,1])
# plt.show()

R_std = 0.5
Q_std = 0.8

def tracker1():
    tracker = KalmanFilter(dim_x=4, dim_z=2)
    dt = 1 # 1 second

    # State transistion function
    tracker.F = np.array([[1,dt,0,0],
                        [0,1,0,0],
                        [0,0,1,dt],
                        [0,0,0,1]])

    # Process noise matrix
    q = Q_discrete_white_noise(dim=2, dt=dt, var=Q_std**2)
    tracker.Q = block_diag(q,q)
    print(tracker.Q)

    # Control matrix is default zero

    # Measurement function
    tracker.H = np.array([[1/0.3048, 0, 0, 0],
                        [0,0,1/0.3047,0]])
    # Converting foot to meters

    # Measurement noise matrix
    # tracker.R = np.array([[5.,0],
    #                     [0,5.]])
    tracker.R = np.eye(2) * R_std**2
    # It is a two cross two matrix because there are two sensor inputs

    # initial guess for sensor data
    tracker.x = np.array([[0,0,0,0]]).T

    # Process covariance matirx
    tracker.P = np.eye(4)*500
    return tracker

### Simulation data
N = 30 
sensor = PosSensor((0,0),(2,2), noise_std=R_std)
zs = np.array([sensor.read() for _ in range(N)])

robot_tracker = tracker1()
mu, cov, _, _ = robot_tracker.batch_filter(zs)

for x,P in zip(mu,cov):
    cov = np.array([[P[0,0], P[2,0],
                     P[0,2],P[2,2]]])
    mean = (x[0,0], x[2,0])
    plot_covariance_ellipse(mean, cov=cov, fc='g', std=3, alpha=0.5)

# Plotting
zs *= .3048 
plt.plot(mu[:,0], mu[:,2])
plt.plot(zs[:,0],zs[:1])
plt.legend(loc=2)