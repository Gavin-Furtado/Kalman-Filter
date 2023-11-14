'''

Author: Gavin Furtado

Reference: Michel Van Biezen lectures
'''

from math_functions_matrix import * 
import matplotlib.pyplot as plt 

gyro_data = {'G_x': [], 'G_y': []}

## Estimated values from Kalman filter ##
prediction = {'G_x': [], 'G_y': []}
kalman_filter = {'G_x': [], 'G_y': []}

file_path = r'C:\Users\gavin\Desktop\Gavin\Self Projects\MPU-6050\IMU\Data collection\data.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

for line in lines:
    data = line.split()

    gyro_data['G_x'].append(float(data[1]))
    gyro_data['G_y'].append(float(data[3]))
    
## Step - Initialization ##
initial_state_matrix = x_initial(1, 1)
initial_control_matrix = u_initial(0)
initial_noise_matrix = w_initial(0)
initial_process_covariance_matrix = p_initial(0.1, 0.1)

for i in range(100):
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
    prediction['G_x'].append(predicted_state_matrix[0][0])
    prediction['G_y'].append(predicted_state_matrix[1][0])

    ## Step 2 - Measurement/Data/Observation from sensors ##
    measured_values = measurements(
        gyro_data['G_x'][i], gyro_data['G_y'][i])

    ## Step 3 - Kalman Gain ##
    kalman_gain_matrix = kalman_matrix(
        predicted_process_covariance_matrix, 0.1, 0.1)

    ## Step 4 - Updation ##
    # Updated Current State Matrix
    updated_state_matrix = calculate_updated_state_matrix(
        matrix_h(), measured_values, kalman_gain_matrix, predicted_state_matrix)

    # Updated Process Covariance Matrix
    updated_process_covariance_matrix = calculate_updated_process_covariance(
        kalman_gain_matrix, matrix_h(), predicted_process_covariance_matrix)

    ## storing kalman filter values in dictionary ##
    kalman_filter['G_x'].append(updated_state_matrix[0][0])
    kalman_filter['G_y'].append(updated_state_matrix[1][0])

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
plt.plot(gyro_data['G_x'], 'ro',color='#FC9C21')
plt.plot(prediction['G_x'], 'g^')
plt.plot(kalman_filter['G_x'], 'r-')
plt.grid(which='major', color='#DDDDDD', linewidth=0.9)
plt.grid(which='minor', color='#EEEEEE', linestyle=':', linewidth=0.6)
plt.minorticks_on()
plt.xlabel('Time period')
plt.ylabel('Gyroscope data (x)')
plt.legend(['measurments', 'predictions', 'kalman filter'])
plt.title('Data from position sensor')
#plt.savefig('position_graph')
plt.show()

# # # velocity graph
# plt.plot([0, 1, 2, 3,4,5,6,7], measurement_velocity, 'ro', color='#FC9C21')
# plt.plot([0, 1, 2, 3,4,5,6,7], prediction['velocity'], 'g^')
# plt.plot([0, 1, 2, 3,4,5,6,7], kalman_filter['velocity'], 'r-')
# plt.grid(which='major', color='#DDDDDD', linewidth=0.9)
# plt.grid(which='minor', color='#EEEEEE', linestyle=':', linewidth=0.6)
# plt.minorticks_on()
# plt.xlabel('Time period')
# plt.ylabel('Velocity (m/s^2)')
# plt.legend(['measurments', 'predictions', 'kalman filter'])
# plt.title('Data from velocity sensor')
# plt.savefig('velocity_graph')
# plt.show()