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

## Matrix H (2x2) ##
def matrix_H():
    return np.array([[1,0],
                     [0,1]])

## Matrix R (2x2) ##
def matrix_R():
    return np.array([[25**2,0],
                     [0,6**2]])  

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

######## Process Covariance Matrix ########
## We assume non-diagonal elements to be zeo, and there is no correlation between
## the errror in position and velocity. This is done to make 
## the calculations simpler
def P_matrix(position_process_error,
                              velocity_process_error):
    return np.array([[position_process_error**2, 0],
                     [0, velocity_process_error**2]])

######## Predicted process covariance matrix ########
## The error matrix Q has been neglected for simplicity
def P_matrix_predicted(delta_T, position_process_error,velocity_process_error):
    term_1 = matrix_A(delta_T) @ P_matrix(position_process_error, velocity_process_error) @ matrix_A(delta_T).T
    # To simplify the calculations
    term_1[0][1]=0
    term_1[1][0]=0
    return term_1

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
def Kalman_Matrix(P_matrix_predicted):
    term_1 = P_matrix_predicted @ matrix_H().T
    term_2 = matrix_H() @ P_matrix_predicted @ matrix_H().T
    term_3 = matrix_R()
    # denominator = term_2 + term_3
    return np.round(term_1 @ np.linalg.inv(term_2 + term_3),3)
    # return np.divide(term_1,denominator)

## New measurements or observations ##
## Here the Z matrix represents the errror in the measurement
## lets assume Z to be 0
def new_measurements(position,velocity):
    C = np.array([[1,0],
              [0,1]])
    prev_Y = np.array([[position],
                       [velocity]])
    return C @ prev_Y

### Testing the functions ###
print(f'Predicted State Matrx = ') 
print(X_predicted(1,4000,280,2,0))

print(f'Predicted Covariance matrix = ')
covariance_predicted = P_matrix_predicted(1,20,5)
print(covariance_predicted)

print(f'Kalman Gain matrix = ')
print(Kalman_Matrix(covariance_predicted))

print(f'New measurement matrix')
print(new_measurements(4260,282))