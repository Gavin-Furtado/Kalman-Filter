### This python file consists of mathematical formulae 
### of Kalman filter algorithms in the state vector/ 
### matrix format

import numpy as np

######## Learning Matrix multiplications ########
# # Defining matrix A
# A = np.array([[2,4],
#               [5,3]])

# # Defining matrix B
# B = np.array([[4,1],
#               [7,9]])

# # printing matrix A
# print(f'The Matrix A = {A}')

# # priniting matrix B
# print(f'The Matrix B = {B}')

# # multiplication of matrix A x B
# print(f'Matrix multiplication using numpy dot funtion = {np.dot(A,B)}')
# print(f'Matrix multiplication using @ = {A @ B}')


################# The Aeroplane example ##############

## Matrix A (2x2) ##
def matrix_A(delta_T):
    A = np.array([[1,delta_T],
                  [0,1]])
    return A

## Matrix B (2x1) ##
def matrix_B(delta_T):
    B = np.array([[0.5*delta_T],
                  [delta_T]])
    return B

## Matrix H (3x3) ##


## State Matrix ##
def state_matrix(position, velocity):
    return np.array([[position],
              [velocity]])
    

## Control Matrix ##
def control_matrix(acceleration):
    return np.array([acceleration])

## Noise Matrix ##
def noise_matrix(noise):
    return np.array([noise])

## Process Covariance Matrix ##

## Step 1 ##
## Predicted State ##
## Xk (predicted) = A.Xk-1 + Buk + wk
def X_predicted(delta_T, position, velocity, acceleration,noise):
    
    term_1 = matrix_A(delta_T) @ state_matrix(position,velocity)
    term_2 = (matrix_B(delta_T) @ control_matrix(acceleration)).reshape(2,1) # Try to understand why reshaping was required
    term_3 = noise_matrix(noise)
    
    predicted_state = term_1 + term_2 +term_3
    return predicted_state


## Kalman Gain Matrix ##



### Testing the functions ###
test = X_predicted(1,4000,280,2,0)
print(test)