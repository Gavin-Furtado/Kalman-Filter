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
                 acceleration=(0.2,0.09), noise_mean=0., noise_std=0.) -> None:
        self.position = np.array(initial_position)
        self.velocity = np.array(initial_velocity)
        self.acceleration = np.array(acceleration)
        self.noise_mean = noise_mean
        self.noise_std = noise_std

    def read(self):
        self.velocity += self.acceleration
        self.position += self.velocity

        noise = np.random.normal(self.noise_mean, self.noise_std,2)
        return self.position + noise, self.velocity + noise, self.acceleration + noise, noise
        #return self.position + np.random.randn(2) * self.noise_std

## Initialise the Sensor
sensor = PositionSensor(noise_mean=0.2, noise_std=2.5)

# Genertion of dummy data
sample_size = 50
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
print(noise_data)

# Plotting
plt.subplot(221)
plt.scatter(time_interval,position_data[:,0],label = 'X-Position')
plt.scatter(time_interval,position_data[:,1],label = 'Y-Position')
plt.xlabel('Time')
plt.ylabel('Position')
plt.title('Position data from sensor')
plt.legend()
# plt.show()

plt.subplot(222)
plt.scatter(time_interval,velocity_data[:,0],label = 'X-Velocity')
plt.scatter(time_interval,velocity_data[:,1],label = 'Y-Velocity')
plt.xlabel('Time')
plt.ylabel('Velocity')
plt.title('Velocity data from sensor')
plt.legend()
#plt.show()

plt.subplot(223)
plt.scatter(time_interval,acceleration_data[:,0],label = 'X-Position')
plt.scatter(time_interval,acceleration_data[:,1],label = 'Y-Position')
plt.title("Acceleration data from sensor")
plt.xlabel('Time') 
plt.ylabel('Acceleration')
# plt.show()

plt.subplot(224)
plt.hist(noise_data.flatten(), bins=50, density=True, alpha=0.75)
plt.title("Gaussian distribution of senosr noise")
plt.xlabel('Noise values') # From Chat GPT
plt.ylabel('Probablity Density')
plt.show()

## Using FilterPy library

## Without FilterPy library
