from math_functions_matrix import *
import matplotlib.pyplot as plt

## Measurements ##
measurement_position = [4000,4260,4550,4860,5110]
measurement_velocity = [280,282,285,286,290]

## Estimated values from Kalman filter ##
prediction = {'position':[], 'velocity':[]}
kalman_filter = {'position':[], 'velocity':[]}

## Step - Initialization ##
initial_state_matrix = X_initial(measurement_position[0],measurement_velocity[0])
initial_control_matrix = U_initial(2)
initial_noise_matrix = W_initial(0)
initial_process_covariance_matrix = P_initial(20,5)

# ## Step 1 - Prediction ##
# # previous_state_matrix = updated_current_state_matrix
# predicted_state_matrix = X_predicted(1,initial_state_matrix,
#                                      initial_control_matrix, initial_noise_matrix)

# # previous_process_covariance_matrix = updated_process_covariance_state_matrix
# predicted_process_covariance_matrix = P_predicted(1,initial_process_covariance_matrix)

# ## Step 2 - Measurement/Data/Observation from sensors ##
# measured_values = measurements(4260,282)

# ## Step 3 - Kalman Gain ##
# kalman_gain_matrix = Kalman_Matrix(predicted_process_covariance_matrix,25,6)

# ## Step 4 - Updation ##
# # Updated Current State Matrix
# updated_state_matrix =calculate_updated_state_matrix(matrix_H(),measured_values,kalman_gain_matrix,predicted_state_matrix)

# # Updated Process Covariance Matrix
# updated_process_covariance_matrix = calculate_updated_process_covariance(kalman_gain_matrix,matrix_H(),
#                                                                          predicted_process_covariance_matrix)

### Printing 1st loop
# print(f'=========Initialization==================')
# print(f'The initial state matrix is')
# print(initial_state_matrix)

# print(f'The initial process covariance matrix is')
# print(initial_process_covariance_matrix)

# print(f'=========Prediction==================')
# print(f'The predicted state matrix is')
# print(predicted_state_matrix)

# print(f'The predicted process covariance matrix is')
# print(predicted_process_covariance_matrix)

# print(f'=========Measurement==================')
# print(f'The measurement matrix is')
# print(measured_values)

# print(f'=========Kalman Gain==================')
# print(f'The kalman gain matrix is')
# print(kalman_gain_matrix)

# print(f'=========Updation==================')
# print(f'The updated state matrix is')
# print(updated_state_matrix)

# print(f'The updated process covariance matrix is')
# print(updated_process_covariance_matrix)

### using for loop

for i in range(5):
    ## Step 1 - Prediction ##
    # previous_state_matrix = updated_current_state_matrix
    if i == 0:
        predicted_state_matrix = X_predicted(1,initial_state_matrix,
                                        initial_control_matrix, initial_noise_matrix)
    else:
        previous_control_matrix = initial_control_matrix
        previous_noise_matrix = initial_noise_matrix
        predicted_state_matrix = X_predicted(1,previous_state_matrix,
                                        previous_control_matrix, previous_noise_matrix)

    # previous_process_covariance_matrix = updated_process_covariance_state_matrix
    if i == 0:
        predicted_process_covariance_matrix = P_predicted(1,initial_process_covariance_matrix)
    else:
        predicted_process_covariance_matrix = P_predicted(1,previous_process_covariance_matrix)

    ## storing prediction value in dictionary ##
    prediction['position'].append(predicted_state_matrix[0][0])
    prediction['velocity'].append(predicted_state_matrix[1][0])

    ## Step 2 - Measurement/Data/Observation from sensors ##
    measured_values = measurements(measurement_position[i],measurement_velocity[i])

    ## Step 3 - Kalman Gain ##
    kalman_gain_matrix = Kalman_Matrix(predicted_process_covariance_matrix,25,6)

    ## Step 4 - Updation ##
    # Updated Current State Matrix
    updated_state_matrix = calculate_updated_state_matrix(matrix_H(),measured_values,kalman_gain_matrix,predicted_state_matrix)

    # Updated Process Covariance Matrix
    updated_process_covariance_matrix = calculate_updated_process_covariance(kalman_gain_matrix,matrix_H(),
                                                                            predicted_process_covariance_matrix)
    
    ## storing kalman filter values in dictionary ##
    kalman_filter['position'].append(updated_state_matrix[0][0])
    kalman_filter['velocity'].append(updated_state_matrix[1][0])

    ## Updated become previous ##
    previous_state_matrix = updated_state_matrix
    previous_process_covariance_matrix = updated_process_covariance_matrix

    print(f'+++++++++++++++++++Iteration number {i} ++++++++++++++++++')
    print(f'=========Prediction==================')
    print(f'The predicted state matrix is')
    print(predicted_state_matrix)

    print(f'The predicted process covariance matrix is')
    print(predicted_process_covariance_matrix)

    print(f'=========Measurement==================')
    print(f'The measurement matrix is')
    print(measured_values)

    print(f'=========Kalman Gain==================')
    print(f'The kalman gain matrix is')
    print(kalman_gain_matrix)

    print(f'=========Updation==================')
    print(f'The updated state matrix is')
    print(updated_state_matrix)

    print(f'The updated process covariance matrix is')
    print(updated_process_covariance_matrix)


## Plotting graphs ##
plt.plot([0,1,2,3,4],measurement_position,'ro')
plt.plot([0,1,2,3,4],prediction['position'],'g^')
plt.plot([0,1,2,3,4],kalman_filter['position'],'r-')
plt.grid(which='both')
plt.xlabel('Time period')
plt.ylabel('Position (m)')
plt.legend(['measurments','predictions','kalman filter'])
plt.show()

# velocity graph
plt.plot([0,1,2,3,4],measurement_velocity,'ro')
plt.plot([0,1,2,3,4],prediction['velocity'],'g^')
plt.plot([0,1,2,3,4],kalman_filter['velocity'],'r-')
plt.grid(which='both')
plt.xlabel('Time period')
plt.ylabel('Velocity (m/s^2)')
plt.legend(['measurments','predictions','kalman filter'])
plt.show()

print(prediction)
print(kalman_filter)