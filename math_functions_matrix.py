### This python file consists of mathematical formulae 
### of Kalman filter algorithms in the state vector/ 
### matrix format

import numpy as np

# Defining matrix A
A = np.array([[2,4],
              [5,3]])

# Defining matrix B
B = np.array([[4,1],
              [7,9]])

# printing matrix A
print(f'The Matrix A = {A}')

# priniting matrix B
print(f'The Matrix B = {B}')

# multiplication of matrix A x B
print(f'Matrix multiplication using numpy dot funtion = {np.dot(A,B)}')
print(f'Matrix multiplication using @ = {A @ B}')

## State Matrix ##

## Process Covariance Matrix ##

## Predicted State ##

## Kalman Gain Matrix ##

## Matrix A (3x3) ##

## Matrix B (3x3) ##

## Matrix H (3x3) ##