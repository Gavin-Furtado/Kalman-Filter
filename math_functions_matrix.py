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

#===============================================================
## Needs work
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
#=======================================================


################# START-OF-STEP-1 ##########################
########### Prediction of new measurements and errors in prediction/process ##

def X_predicted(delta_T, position, velocity, acceleration,noise):    
    '''
    This function predicts the state matrix
    In simple terms predicts the next value of the measurement 
    that would come from the sensors.

    The formula in matrix format;
    Xk (predicted) = A.Xk-1 + Buk + wk

    inputs = sampling time, position, velocity, acceleration, noise
    output = position, velocity (predicted)  
    '''
    term_1 = matrix_A(delta_T) @ state_matrix(position,velocity)
    term_2 = (matrix_B(delta_T) @ control_matrix(acceleration)).reshape(2,1) # Try to understand why reshaping was required
    term_3 = noise_matrix(noise)
    
    predicted_state = term_1 + term_2 +term_3
    return predicted_state

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

def new_measurements(position,velocity):
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
def Kalman_Matrix(P_matrix_predicted):
    '''
    Calculates the kalman gain matrix,
    Kalman gain determines the amount of weight given 
    to the measured value or the predicted value.

    inputs = predicted process covariance matrix, errors in observation
    output = Kalman Gain Matrix 
    '''
    term_1 = P_matrix_predicted @ matrix_H().T
    term_2 = matrix_H() @ P_matrix_predicted @ matrix_H().T
    term_3 = matrix_R(25,6)
    # denominator = term_2 + term_3
    return np.round(term_1 @ np.linalg.inv(term_2 + term_3),3)
    # return np.divide(term_1,denominator)

################# END-OF-STEP-3 ##########################

### Testing the functions ###
print(f'Predicted State Matrx = ') 
predicted_state_matrix = X_predicted(1,4000,280,2,0)
print(predicted_state_matrix)

print(f'Predicted Covariance matrix = ')
covariance_predicted = P_matrix_predicted(1,20,5)
print(covariance_predicted)

print(f'Kalman Gain matrix = ')
kalman_gain_matrix = Kalman_Matrix(covariance_predicted)
print(kalman_gain_matrix)

print(f'New measurement matrix')
new_measured_values = new_measurements(4260,282)
print(new_measured_values)

## Calculating current state ##
def current_state():
    term_1 = matrix_H() @ predicted_state_matrix
    term_2 = new_measured_values - term_1
    term_3 = kalman_gain_matrix @ term_2
    return predicted_state_matrix + term_3

print(f'Current/updated state matrix')
current_state_matrix = current_state()
print(current_state_matrix)

## Updating process covariance matrix ##
def updated_process_covariance():
    term_1 = kalman_gain_matrix @ matrix_H()
    term_2 = np.array([[1,0],[0,1]]) - term_1
    return term_2 @covariance_predicted

print(f'Updated Process Covariance Matrix is')
current_process_covariance = updated_process_covariance()
print(current_process_covariance)

# ### 2nd Iteration ###
# ## Predicted State Matrix ##
# state_matrix_2 = X_predicted(1,current_state_matrix[0][0],
#             current_state_matrix[1][0],2,0)
# print(f'======2nd iteration======')
# print(f'==State Matrix==')
# print(state_matrix_2)

# ## Predicted Process Covarince Matrix ##
# predicted_covar_2 = P_matrix_predicted(1,current_process_covariance[0][0],
#                                        current_process_covariance[1][1])
# print(f'======2nd iteration======')
# print(f'==Predicted Process Covariance Matrix==')
# print(predicted_covar_2)