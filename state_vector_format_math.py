### This python file consists of mathematical formulae 
### of Kalman filter algorithms in the state vector/ 
### matrix format

import numpy as np

A = np.array([[2,4],
              [5,3]])
A = np.matrix(A)
B = np.multiply(A,A)

print(B)


