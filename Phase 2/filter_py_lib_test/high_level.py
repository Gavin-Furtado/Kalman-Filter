'''
High level implementation of Kalman Filter algorithm


Author
------
Gavin Furtado

AOCS Engineer
'''

import electronic_sensors as es 
import graph as gr
import kf_computation as kal
import matplotlib.pyplot as plt
import numpy as np
from constants import dt

'''
Things to go
1. Check the calculations, the graphs tell there is something wrong
    When you use sample size of 20 it is clear, as the sample size increases the kalman filter algorithm 
    starts building trust with predicted values over measured values
2. Make the code more professional
    a. Proper names for modules, variables, classes
    b. docstrings
    c. github documentation
3. Think of GUI if possible
'''


def visulaise_data(position, velocity, acceleration, noise, display_graph=bool):
    '''
    Summary

    Notes
    -----
    Array length is eqaul to the sample size that is user defined.
    The dimensions of the array are constant i.e. 2-dimensions.

    Attributes
    ----------
    position : a 2D array, x-cordinate & y-cordinate
    velocity : a 2D array, x-dimension & y-dimension
    acceleration : a 2D array, x-dimension & y-dimension
    display_graph : boolean - True or False

    Returns
    -------
    '''
    # Creating a single graph window
    plt.figure(figsize=(10,5))

    # Creating instance of PlotGraph class
    position_graph =gr.PlotGraph(plot_number=221, y1_data=position[:,0], y2_data=position[:,1],
                                title='Position data from sensor', xlabel='Time (s)', ylabel='Position (m)',
                                label_1='X-position',label_2='Y-position')

    velocity_graph = gr.PlotGraph(plot_number=222, y1_data=velocity[:,0], y2_data=velocity[:,1],
                                title='Velocity data from sensor', xlabel='Time (s)', ylabel='Velocity (m/s)',
                                label_1='X-velocity', label_2='Y-velocity')

    acceleration_graph = gr.PlotGraph(plot_number=223, y1_data=acceleration[:,0], y2_data=acceleration[:,1],
                                title='Acceleration data from sensor', xlabel='Time (s)', ylabel='Acceleration (m/s^2)',
                                label_1='X-Acceleration', label_2='Y-Acceleration')

    gaussian_noise_graph = gr.PlotGraph(plot_number=224, y1_data=noise, title='Gaussian Noise Distribution',
                                        xlabel='Noise values', ylabel='Probability Density',
                                        bins=50, alpha=0.7, density=True)

    # Calling methods of class PlotGraph 
    position_graph.scatter_plot()
    velocity_graph.scatter_plot()
    acceleration_graph.scatter_plot()
    gaussian_noise_graph.gaussian_plot()

    # #Display graph
    plt.suptitle('Accelerometer Data')
    plt.tight_layout()
    plt.show(block=display_graph)


data = {'Current State':[],'Predicted State':[],'Updated State':[]}

def main():
    '''
    The main function of the code.

    It contains the high level logic.
    '''
    ## Sensor data ##
    sensor = es.PositionSensor(noise_mean=1.0, noise_std=1.5, dt=dt ,sample_size=10)
    position, velocity, acceleration, noise = sensor.data_set()

    ## Data Visualisation ##
    visulaise_data(position, velocity, acceleration, noise, False)

    ## Initalisation ##
    initialisation = kal.kalman_initial(position,velocity, acceleration)
    P_initial = initialisation.P_initial(2,1,8,7)
    X_initial = initialisation.X_initial()
    
    P_prev = P_initial
    X_prev = X_initial
    
    ## Kalman Filter Loop ##
    for idx, (pos,vel,acc) in enumerate(zip(position,velocity,acceleration)):    
        state_matrix = np.array([[pos[0]],
                                 [pos[1]],
                                 [vel[0]],
                                 [vel[1]]])
        #print(f'The state matrix in the loop= {state_matrix}')
        control_matrix = np.array([[acc[1]],
                                   [acc[1]]]) 

        # predict = kal.Prediction(state_matrix,None,control_matrix)
        # predict_state = predict.X_predicted()
        
        # Prediction stage
        # predict = kal.Prediction(state_matrix,P_prev,control_matrix)
        predict = kal.Prediction(X_prev,P_prev,control_matrix)
        predict_state = predict.X_predicted()
        predict_P = predict.P_predicted()

        # Kalman Gain
        R = kal.R_matrix(3,1,2,1)
        K = kal.KalmanGain(predict_P,R)
        
        # Measurement input
        Y = kal.measurement_input(state_matrix)

        # Updation
        update = kal.updation(K,Y,predict_P,predict_state)
        updated_state = update.X_updated()
        updated_P = update.P_updated()      

        X_prev = updated_state
        P_prev = updated_P
                
        # Storing values in a dictionary
        data['Current State'].append(state_matrix)
        data['Predicted State'].append(predict_state)
        data['Updated State'].append(updated_state)

    ## Conversion to arrays for ease of plotting
    data_current_state = np.array(data['Current State'])
    data_predicted_state = np.array(data['Predicted State'])
    data_updated_state = np.array(data['Updated State'])
    
    '''
    This is the way to extract data from dictionary that would fit the 
    class PlotGraph
    # print(data['Current State'],temp_data[:,0,0])
    '''
        
    ## Testing the data on graph
    plt.figure(figsize=(10,5))
    compare_x_pos = gr.PlotGraph(221,data_current_state[:,0,0], data_predicted_state[:,0,0] , data_updated_state[:,0,0],
                    'Position in X direction','time(s)','position(m)',
                    'Measurement','Prediction', 'Kalman filter')
    compare_x_pos.scatter_plot()
    compare_x_pos.line_plot()
    
    compare_y_pos = gr.PlotGraph(222,data_current_state[:,1,0], data_predicted_state[:,1,0] , data_updated_state[:,1,0],
                    'Position in Y direction','time(s)','position(m)',
                    'Measurement','Prediction', 'Kalman filter')
    compare_y_pos.scatter_plot()
    compare_y_pos.line_plot()

    # plt.figure(figsize=(10,5))
    compare_x_vel = gr.PlotGraph(223,data_current_state[:,2,0], data_predicted_state[:,2,0] , data_updated_state[:,2,0],
                    'Velocity in X direction','time(s)','velocity(m/s)',
                    'Measurement','Prediction', 'Kalman filter')
    compare_x_vel.scatter_plot()
    compare_x_vel.line_plot()
    
    compare_y_vel = gr.PlotGraph(224,data_current_state[:,3,0], data_predicted_state[:,3,0] , data_updated_state[:,3,0],
                    'Velocity in Y direction','time(s)','velocity(m/s)',
                    'Measurement','Prediction', 'Kalman filter')
    compare_y_vel.scatter_plot()
    compare_y_vel.line_plot()

    plt.suptitle('Kalman Filter Algorithm on Accelerometer data')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()