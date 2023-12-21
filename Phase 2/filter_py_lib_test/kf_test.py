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

print(compute_dog_data(0.5,0.2))


