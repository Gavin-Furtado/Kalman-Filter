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

##### Defining matrices #######
##### Need to make this reusable ######
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

## Errors in measurement ##
## delta_x, delta_Vx
## Matrix R (2x2) ##
def matrix_R(position_err,velocity_err):
    return np.array([[position_err**2,0],
                     [0,velocity_err**2]])  


################# START-OF-INITIALIZATION ##########################

######## Initial State Matrix ##############
def X_initial(position,acceleration):
    return np.array([[position],[acceleration]])

## Initial Control Matrix ##
def U_initial(acceleration):
    return np.array([acceleration])

## Initial Noise Matrix ##
def W_initial(noise):
    return np.array([noise])
    
######## Initial Process Covariance Matrix ########
## We assume non-diagonal elements to be zeo, and there is no correlation between
## the errror in position and velocity. This is done to make 
## the calculations simpler
def P_initial(position_process_error, velocity_process_error):
    '''
    Initial values for process covariance matrix
    '''
    return np.array([[position_process_error**2, 0],
                     [0, velocity_process_error**2]])

################# END-OF-INITIALIZATION ##########################


################# START-OF-STEP-1 ##########################
########### Prediction of new measurements and errors in prediction/process ##

def X_predicted(delta_T, X_prev, control_matrix, noise_matrix):    
    '''
    This function predicts the state matrix
    In simple terms predicts the next value of the measurement 
    that would come from the sensors.

    The formula in matrix format;
    Xk (predicted) = A.Xk-1 + Buk + wk

    inputs = sampling time, position, velocity, acceleration, noise
    output = position, velocity (predicted)  
    '''
    term_1 = matrix_A(delta_T) @ X_prev
    term_2 = (matrix_B(delta_T) @ control_matrix).reshape(2,1) # Try to understand why reshaping was required
    term_3 = noise_matrix
    
    return term_1 + term_2 +term_3
    

######## Predicted process covariance matrix ########
## The error matrix Q has been neglected for simplicity
def P_predicted(delta_T, P_prev):
    '''
    This function calculate predicted process covariance martix
    In simple terms calculates the error in estimates or process

    The formula in matrix form is;
    Pkp = A.Pk-1.A^T + Qk

    inputs = matrix A, previous predicted covarinace matrix
    output = predicted covariance matrix
    '''
    term_1 = matrix_A(delta_T) @ P_prev @ matrix_A(delta_T).T
    # To simplify the calculations
    term_1[0][1]=0
    term_1[1][0]=0
    return term_1 

################# END-OF-STEP-1 ##########################

################# START-OF-STEP-2 ##########################

######### New measurements or observations ##########
## Here the Z matrix represents the error in the measurement
## lets assume Z to be 0

def measurements(position,velocity):
    '''
    Takes the measurement data from the sensors and
    converts them into a matrix format

    input = position, velocity
    output = [[position], [velocity]]
    '''
    C = np.array([[1,0],
              [0,1]])
    prev_Y = np.array([[position],
                       [velocity]])
    return C @ prev_Y

################# END-OF-STEP-2 ##########################


################# START-OF-STEP-3 ##########################

## Kalman Gain Matrix ##
def Kalman_Matrix(P_matrix_predicted,position_err,velocity_err):
    '''
    Calculates the kalman gain matrix,
    Kalman gain determines the amount of weight given 
    to the measured value or the predicted value.

    inputs = predicted process covariance matrix, errors in observation(position,velocity)
    output = Kalman Gain Matrix 
    '''
    term_1 = P_matrix_predicted @ matrix_H().T
    term_2 = matrix_H() @ P_matrix_predicted @ matrix_H().T
    term_3 = matrix_R(position_err,velocity_err)
    # denominator = term_2 + term_3
    return np.round(term_1 @ np.linalg.inv(term_2 + term_3),3)
    # return np.divide(term_1,denominator)

################# END-OF-STEP-3 ##########################

################# START-OF-STEP-4 ##########################

#### Updating the state matrix and process covarinace matrix #######
## Calculating current state ##
def calculate_updated_state_matrix(matrix_H, new_measurements, k_gain, predicted_state):
    '''
    This function updates the sate matrix for the next iteration;

    inputs: predicted state, H-matrix, new measured values,
            kalman gain
    output: updated state matrix
    '''
    term_1 = matrix_H @ predicted_state
    term_2 = new_measurements - term_1
    term_3 = k_gain @ term_2
    updated_state_matrix = predicted_state + term_3
    return updated_state_matrix

## Updating process covariance matrix ##
def calculate_updated_process_covariance(k_gain,matrix_H,predicted_process_covar):
    '''
    This function updates the process covariance matrix

    inputs: kalman gain, H-matrix, predicted covarinace matrix
    
    Local variables: Identity matrix,
            
    output: Updated covariance matrix
    '''
    term_1 = k_gain @ matrix_H
    term_2 = np.array([[1,0],[0,1]]) - term_1
    return term_2 @ predicted_process_covar
     

################# END-OF-STEP-4 ##########################



