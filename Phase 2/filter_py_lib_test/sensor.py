'''
Modue name
----------
sensor

Module summary
--------------
Module that simulates a real world electronic sensor

Usage
-----
This module is used to generate a functional model the real world sensors 
such as accelerometer and gyroscope.
You will be able to obtain a dataset of the measurements of respective sensors.

Example
-------
Here is an example of how to use this module in projects.
```python
import sensor as sn

sensor = sn.PositionSensor(noise_mean=0.2, noise_std=1.5, dt=1,sample_size=50)
position, velocity, acceleration, noise = sensor.data_set()
```python

Author
------
Gavin Furtado

Role
----
AOCS Engineer
'''

import numpy as np

class PositionSensor(object):
    '''
    Represent a real world position sensor/accelerometer that
    measures position, velocity and accleration of an object. 
    This sensor has gaussian noise added to its measurements.

    Attributes
    ----------  
    position : float
        Cooridnates of the moving object in x,y dimensions
        default values = (0,0)
    
    velocity : float
        Velocity of the moving object in x,y dimensions 
        default values = (0,0) 
    
    noise_std : float  
        Standard deviation of gaussian noise
        default value = 0

    noise_mean : float
        Mean value of the gaussian noise
        default value = 0 

    sample size: int
        Number of readings/measurements taken by the sensor
    
    Methods
    -------
    read():
        Returns the instanteous position, velocity, acceleration of the 
        moving object and also returns the noise and standard 
        deviation of noise.
    
    data_set():
        Returns the complete data set based on the requested sample
        size. It returns the separarte data set of position, velocity,
        acceleration and noise

    Example
    -------
    Here is an example of how to use this module in projects.
    ```python
    import sensor as sn

    sensor = sn.PositionSensor(noise_mean=0.2, noise_std=1.5, dt=1,sample_size=50)
    
    position, velocity, acceleration, noise = sensor.data_set()
    '''
    def __init__(self, initial_position=(0.,0.), initial_velocity=(0.,0.), 
                 acceleration=(0.2,0.09),dt=0., noise_mean=0., noise_std=0.,
                 sample_size=0) -> None:
        '''
        Intitalisation function of the class Position Sensor

        Attributes
        ----------
        position : array
        velocity : array
        acceleration : array
        dt : array
        noise_mean : float
        noise_std : float
        sample_size : int
        '''
        self.position = np.array(initial_position)
        self.velocity = np.array(initial_velocity)
        self.acceleration = np.array(acceleration)
        self.dt = np.array(dt)
        self.noise_mean = noise_mean
        self.noise_std = noise_std
        self.sample_size = sample_size

    def read(self):
        '''
        Summary
        -------
        This functions measures the position, velocity and 
        acceleration of the object.

        Parameters
        -----------
        None

        Returns
        -------
        position, velocity, acceleration, noise
        Single 2-Dimensional arrays
        '''
        self.velocity += self.acceleration*self.dt  
        self.position += self.velocity*self.dt 

        noise = np.random.normal(self.noise_mean, self.noise_std,2) 
        ## Is this error in measurement(R) or error in process (P)  
        ## Probably error in measurement(R)                                                  

        return self.position + noise, self.velocity + noise, self.acceleration + noise, noise
        #return self.position + np.random.randn(2) * self.noise_std
    
    def data_set(self):
        '''
        
        Creates a data set of position, velocity, acceleration and noise.
        
        Parameters
        ----------
        None
        
        Returns
        -------
        postion_data : An array of 2-Dimensional arrays
            Array containing X and Y position coordinates.
        velocity_data : An array of 2-Dimensional arrays
            Array containing X and Y velocities.
        acceleration_data : An array of 2-Dimensional arrays
            Array containing X and Y accelerations.
        noise_data : An array of 2-Dimensional arrays
            Array containing Gaussian noise.
        '''
        position_data = np.zeros([self.sample_size,2])
        velocity_data = np.zeros([self.sample_size,2])
        acceleration_data = np.zeros([self.sample_size,2])
        noise_data = np.zeros([self.sample_size,2])

        for i in range(self.sample_size):
            position, velocity, acceleration, noise = self.read()
            position_data[i] = position
            velocity_data[i] = velocity
            acceleration_data[i] = acceleration
            noise_data[i] = noise
        return position_data, velocity_data, acceleration_data, noise_data



