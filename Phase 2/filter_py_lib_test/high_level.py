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
1. verify the Process covarinace matrix, the last two rows do not seem to change
2. build kalman filter class
3. Measurement matrix Y
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
    plt.tight_layout()
    plt.show(block=display_graph)


data = {'Current State':[],'Predicted State':[]}

def main():
    '''
    The main function of the code.

    It contains the high level logic.
    '''
    ## Sensor data ##
    sensor = es.PositionSensor(noise_mean=0.5, noise_std=1.5, dt=dt ,sample_size=50)
    position, velocity, acceleration, noise = sensor.data_set()

    ## Data Visualisation ##
    visulaise_data(position, velocity, acceleration, noise, True)

    ## Initalisation ##
    covar = kal.kalman_initial(position,velocity, acceleration)
    P_initial = covar.P_initial(2,1,5,3)
    
    # P_predict = kal.Prediction(None,None,None)
    # print(P_predict.P_predicted(P_initial))

    P_prev = P_initial

    ## Kalman Filter Loop ##
    for idx, (pos,vel,acc) in enumerate(zip(position,velocity,acceleration)):    
        state_matrix = np.array([[pos[0]],
                                 [pos[1]],
                                 [vel[0]],
                                 [vel[1]]])
        
        control_matrix = np.array([[acc[1]],
                                   [acc[1]]]) 

        # predict = kal.Prediction(state_matrix,None,control_matrix)
        # predict_state = predict.X_predicted()
        
        # Prediction stage
        predict = kal.Prediction(state_matrix,P_prev,control_matrix)
        predict_state = predict.X_predicted()
        predict_P = predict.P_predicted()

        '''
        Now you need kalman gain
        '''

        # Updation
        P_prev = predict_P
        print(predict_P, P_prev)
        '''
        The last two rows are not changing
        '''
        
        '''
        Brainstroming ideas
        ----

        predicted_P = predict.P_predicted()
        if idx == 0:
            predict_covar = predict.P_predicted(P_initial)
            pass
        else: 
            predict_covar = predict.P_predicted(P_prev)

        P_prev = P_predicted
        '''

        # Storing values in a dictionary
        data['Current State'].append(state_matrix)
        data['Predicted State'].append(predict_state)

    ## Conversion to arrays for ease of plotting
    data_current_state = np.array(data['Current State'])
    data_predicted_state = np.array(data['Predicted State'])
    
    '''
    This is the way to extract data from dictionary that would fit the 
    class PlotGraph
    # print(data['Current State'],temp_data[:,0,0])
    '''
        
    ## Testing the data on graph
    plt.figure(figsize=(10,5))
    compare = gr.PlotGraph(111,data_current_state[:,0,0], data_predicted_state[:,0,0] ,
                    'Position in X direction','time','position',
                    'current state','predicted state')
    compare.scatter_plot()
    plt.show()


    # kal.KalmanGain()

    # kal.updation()

    '''
    I also want a class that just loops over the data
    '''

    '''
    Classes of the module kalman filter

    Prediction

    Kalman Gain

    Updation of State matrix
    
    '''

if __name__ == '__main__':
    main()




######## Converting sensor data into matrix format ##########

# matrix = kal.kalman_initial(position, velocity, acceleration)
# # print(matrix.P_initial(None,None, None,None))

# ## Step 0 - Initial State ##


# ## Previous State ##

# ## Step 1 - Predicted State ##
# prediction = kal.Prediction(matrix.X_initial(), None, matrix.u_initial())
# print(prediction.X_predicted())

# ## Step 2 - Measurement from sensor ##

# ## Step 3 - Kalman Gain ##

# ## Step 4 - Update measurement & Kalman Gain ##