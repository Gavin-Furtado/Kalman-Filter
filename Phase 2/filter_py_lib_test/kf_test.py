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

## To do list

# 2. Solve Github problem
# 3. Code using own style
# 4. Prepare state matrix

import math
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt

## dummy data - tracking a dog
def compute_dog_data(measurement_var, process_var, count=1, dt=1):
    # initial value for position and velocity
    position, velocity = 0.,1.

    # calculated standard deviation
    measurement_std = math.sqrt(measurement_var)
    process_std = math.sqrt(process_var)
    
    position_data, measurement_data = [], []
    for i in range(count):
        # calculating position and veocity
        v = velocity + (randn() * process_std)
        position += v*dt
        position_data.append(position)
        measurement_data.append(position + randn() * measurement_std)
    
    return np.array(position_data), np.array(measurement_data)

# print(compute_dog_data(0.5,0.2))

## dummy data class - tracking a robot
## A model of real world object: electronic sensor
class PositionSensor(object):
    '''
    Attributes: self, position, velocity, noise standard deviation
    
    Methods: read
    '''
    def __init__(self, initial_position=(0.,0.), initial_velocity=(0.,0.), 
                 acceleration=(0.2,0.09),dt=0., noise_mean=0., noise_std=0.) -> None:
        self.position = np.array(initial_position)
        self.velocity = np.array(initial_velocity)
        self.acceleration = np.array(acceleration)
        self.dt = np.array(dt)
        self.noise_mean = noise_mean
        self.noise_std = noise_std

    def read(self):
        self.velocity += self.acceleration*self.dt  
        self.position += self.velocity*self.dt 

        noise = np.random.normal(self.noise_mean, self.noise_std,2) 
        ## Is this error in measurement(R) or error in process (P)                                                    

        return self.position + noise, self.velocity + noise, self.acceleration + noise, noise
        #return self.position + np.random.randn(2) * self.noise_std

## Initialise the Sensor
sensor = PositionSensor(noise_mean=0.2, noise_std=1.5, dt=1)

# Genertion of dummy data
sample_size = 50     # size of the data set
position_data = np.zeros((sample_size,2))
velocity_data = np.zeros((sample_size,2))
acceleration_data = np.zeros((sample_size,2))
noise_data = np.zeros((sample_size,2))

for i in range(sample_size):
    position, velocity, acceleration, noise = sensor.read()
    position_data[i] = position
    velocity_data[i] = velocity
    acceleration_data[i] = acceleration
    noise_data[i] = noise

time_interval = np.arange(sample_size) # Create an array for x-axis, use either range() or np.arange()

class PlotGraph(object):
    def __init__(self, plot_number, x_data,y1_data,y2_data, title, xlabel, ylabel, label_1,label_2,
                 bins, alpha, density):
        self.plot_number = plot_number
        self.x_data = x_data
        self.y1_data = y1_data
        self.y2_data = y2_data
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.label_1 = label_1
        self.label_2 = label_2
        self.bins = bins
        self.alpha = alpha
        self.density = density
    
    def scatter_plot(self):
        plt.subplot(self.plot_number)
        plt.scatter(self.x_data, self.y1_data, label = self.label_1)
        plt.scatter(self.x_data, self.y2_data, label = self.label_2)
        plt.grid(True, which='both',linewidth=0.5)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        plt.legend()
    
    def gaussian_plot(self):
        plt.subplot(self.plot_number)
        plt.hist(self.y1_data.flatten(), self.bins, density=self.density, alpha=self.alpha)
        plt.grid(True, which='both',linewidth=0.5)
        plt.title(self.title)
        plt.xlabel(self.xlabel) 
        plt.ylabel(self.ylabel)
        
#Creating a single graph window
plt.figure(figsize=(10,5))

#Creating instance of PlotGraph class
position_graph=PlotGraph(221,time_interval,position_data[:,0],position_data[:,1],
           'Position data from sensor', 'Time', 'Position','X-position','Y-position', None, None, None)

velocity_graph=PlotGraph(222,time_interval,velocity_data[:,0],velocity_data[:,1],
           'Velocity data from sensor', 'Time', 'Velocity','X-position','Y-position', None, None, None)

acceleration_graph=PlotGraph(223,time_interval,acceleration_data[:,0],acceleration_data[:,1],
           'Acceleration data from sensor', 'Time', 'Velocity','X-position','Y-position', None, None, None)

gaussian_noise_graph = PlotGraph(224, None, noise_data, None, 'Gaussian Noise Distribution',
                                 'Noise values', 'Probability Density', None, None, 50, 0.7, True)

#Calling scatter_plot() method of class PlotGraph 
position_graph.scatter_plot()
velocity_graph.scatter_plot()
acceleration_graph.scatter_plot()
gaussian_noise_graph.gaussian_plot()

#Display graph
# plt.tight_layout()
# plt.show()

# print(position_data)
# print(velocity_data)
# print(acceleration_data)
# print(noise_data)

print(position_data[3])
print(velocity_data[3])

X = np.array([[position_data[3][0]],[position_data[3][1]],
              [velocity_data[3][0]],[velocity_data[3][1]]])
print(X.size)

## Using FilterPy library



###### Without FilterPy library ######
'''
X = State Matrix
u = Control variable matrix
w = predicted state noise matrix

P = Process covariance matrix (Error in process)
Q = Process noise covariance matrix 
R = Sensor noise covariance matrix (Error in measurement)

Y = Measurement of state
K = Kalman Gain

dt = Time period
A,B = Adaptation matrix
'''

## Set up
# dt = 1.

# X = np.array([[, y],
#              [x', y']])
# P = 
# A = np.array([[1, dt],
#               [0, 1]])
# B = np.array([[0.5*dt**2],
#               [dt**2]])
# u = 0

# H = 'TBD'

# R = 
# Q =
## Step 0 - Initial State ##


## Previous State ##

## Step 1 - Predicted State ##
class Prediction(object):
    def __init__(self, X_previous, P_previous, dt=2., u=0, w=0, Q=0) -> None:
        self.X_previous = X_previous
        self.u = u
        self.w = w
        self.dt = dt
        self.P_previous = P_previous
        self.Q = Q

    def A_matrix(self):
        # Computing Matrix A, B
        X_shape = self.X_previous.shape  #(4,1)

        if X_shape[0] == 4: 
            self.A = np.array([[1., 0., self.dt, 0.],
                               [0., 1., 0., self.dt],
                               [0., 0., 1., 0.],
                               [0., 0., 0., 1.]])
        elif X_shape[0] == 2:
            self.A = np.array([[1., self.dt],
                               [0., 1.]]) 
            
        elif X_shape[0] == 1:
            self.A = np.array([[1.]])
        return self.A

    def B_matrix(self):
        u_shape = self.u.shape

        if u_shape[0] == 1: 
            self.B = np.array([[0.5*self.dt**2],
                               [self.dt**2]])

        elif u_shape[0] == 2:
            self.B = np.array([[0.5*self.dt**2, 0.],
                               [0., 0.5*self.dt**2],
                               [self.dt, 0.],
                               [0., self.dt]])
        return self.B

    def X_predicted(self):
        pass

    def P_predicted(self):
        pass

predict = Prediction(X,0)
print(predict.A_matrix())

## Step 2 - Measurement from sensor ##

## Step 3 - Kalman Gain ##

## Step 4 - Update measurement & Kalman Gain ##
