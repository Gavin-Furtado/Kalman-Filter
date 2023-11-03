'''
This module performs the computation of the 
Kalman filter for two variables. In this 
example we have considered the position and
valocity of an aeroplane

Author: Gavin Furtado

Reference: Michel Van Biezen lectures
'''

from math_functions_matrix import *  # pylint: disable=unused-wildcard-import
import matplotlib.pyplot as plt
# from tabulate import tabulate

## Measurements ##
measurement_position = [4260, 4550, 4860, 5110]
measurement_velocity = [282, 285, 286, 290]

## Estimated values from Kalman filter ##
prediction = {'position': [], 'velocity': []}
kalman_filter = {'position': [], 'velocity': []}

## Step - Initialization ##
initial_state_matrix = x_initial(4000, 280)
initial_control_matrix = u_initial(2)
initial_noise_matrix = w_initial(0)
initial_process_covariance_matrix = p_initial(20, 5)

# using for loop

for i in range(4):
    ## Step 1 - Prediction ##
    # previous_state_matrix = updated_current_state_matrix
    if i == 0:
        predicted_state_matrix = x_predicted(1, initial_state_matrix,
                                             initial_control_matrix, initial_noise_matrix)
    else:
        previous_control_matrix = initial_control_matrix
        previous_noise_matrix = initial_noise_matrix
        predicted_state_matrix = x_predicted(1, previous_state_matrix,  # pylint: disable=used-before-assignment
                                             previous_control_matrix, previous_noise_matrix)

    # previous_process_covariance_matrix = updated_process_covariance_state_matrix
    if i == 0:
        predicted_process_covariance_matrix = p_predicted(
            1, initial_process_covariance_matrix)
    else:
        predicted_process_covariance_matrix = p_predicted(
            1, previous_process_covariance_matrix)  # pylint: disable=used-before-assignment

    ## storing prediction value in dictionary ##
    prediction['position'].append(predicted_state_matrix[0][0])
    prediction['velocity'].append(predicted_state_matrix[1][0])

    ## Step 2 - Measurement/Data/Observation from sensors ##
    measured_values = measurements(
        measurement_position[i], measurement_velocity[i])

    ## Step 3 - Kalman Gain ##
    kalman_gain_matrix = kalman_matrix(
        predicted_process_covariance_matrix, 25, 6)

    ## Step 4 - Updation ##
    # Updated Current State Matrix
    updated_state_matrix = calculate_updated_state_matrix(
        matrix_h(), measured_values, kalman_gain_matrix, predicted_state_matrix)

    # Updated Process Covariance Matrix
    updated_process_covariance_matrix = calculate_updated_process_covariance(
        kalman_gain_matrix, matrix_h(), predicted_process_covariance_matrix)

    ## storing kalman filter values in dictionary ##
    kalman_filter['position'].append(updated_state_matrix[0][0])
    kalman_filter['velocity'].append(updated_state_matrix[1][0])

    ## Updated become previous ##
    previous_state_matrix = updated_state_matrix
    previous_process_covariance_matrix = updated_process_covariance_matrix

    print(f'+++++++++++++++++++Iteration number {i} ++++++++++++++++++')
    print('=========Prediction==================')
    print('The predicted state matrix is')
    print(predicted_state_matrix)

    print('The predicted process covariance matrix is')
    print(predicted_process_covariance_matrix)

    print('=========Measurement==================')
    print('The measurement matrix is')
    print(measured_values)

    print('=========Kalman Gain==================')
    print('The kalman gain matrix is')
    print(kalman_gain_matrix)

    print('=========Updation==================')
    print('The updated state matrix is')
    print(updated_state_matrix)

    print('The updated process covariance matrix is')
    print(updated_process_covariance_matrix)


## Plotting graphs ##
plt.plot([0, 1, 2, 3], measurement_position, 'ro')
plt.plot([0, 1, 2, 3], prediction['position'], 'g^')
plt.plot([0, 1, 2, 3], kalman_filter['position'], 'r-')
plt.grid(which='major', color='#DDDDDD', linewidth=0.9)
plt.grid(which='minor', color='#EEEEEE', linestyle=':', linewidth=0.6)
plt.minorticks_on()
plt.xlabel('Time period')
plt.ylabel('Position (m)')
plt.legend(['measurments', 'predictions', 'kalman filter'])
plt.show()

# # velocity graph
plt.plot([0, 1, 2, 3], measurement_velocity, 'ro')
plt.plot([0, 1, 2, 3], prediction['velocity'], 'g^')
plt.plot([0, 1, 2, 3], kalman_filter['velocity'], 'r-')
plt.grid(which='major', color='#DDDDDD', linewidth=0.9)
plt.grid(which='minor', color='#EEEEEE', linestyle=':', linewidth=0.6)
plt.minorticks_on()
plt.xlabel('Time period')
plt.ylabel('Velocity (m/s^2)')
plt.legend(['measurments', 'predictions', 'kalman filter'])
plt.show()

# print(f'Predicted values')
# print(tabulate(prediction, headers='keys', tablefmt= 'pretty'))

# print(f'Kalman filter values')
# print(tabulate(kalman_filter, headers='keys', tablefmt= 'pretty'))
