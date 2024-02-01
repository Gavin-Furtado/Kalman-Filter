'''
Module name
-----------
constants 

Module Summary
--------------
This module is a collection of constants that are used across all modules in this project.

Constants
---------
1. dt(float): The time interval between two measurements in seconds.

Usage
-----
This module is the central location to store all the important constant 
data. You can change and control all the contants by changing it here 
and it will reflect in all the modules you used it. This helps in maintianing
synchronicity across the simulation.

Example
-------
To use this time interval in other modules, follow the example below
```python
from constants import dt

# Python code using dt constant
sensor = es.PositionSensor(noise_mean=0.5, noise_std=1.5, dt=dt ,sample_size=50)

```python 

Author
------
Gavin Furtado

Role
-----
AOCS Engineer
'''

## The time interval in seconds
dt = 1.