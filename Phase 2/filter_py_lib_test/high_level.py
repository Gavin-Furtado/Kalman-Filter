import electronic_sensors as es 
import graph as gr
import matplotlib.pyplot as plt

######### Sensor Data        #############
sensor = es.PositionSensor(noise_mean=0.5, noise_std=1.5, dt=1,sample_size=50)
position, velocity, acceleration, noise = sensor.data_set()

######### Data visualisation #############

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
# plt.tight_layout()
# plt.show()

######## Converting sensor data into matrix format ##########

print(position[3])
print(velocity[3])
print(acceleration[3])
'''
MatrixForm(position_x,position_y
           velocity_x,velocity_y
           acceleration_x, acceleration_y)

MatrixForm.X_initial()
MatricForm.u_initial()
MatrixForm.P_initial() - Maybe
'''

# X = np.array([[position_data[3][0]],[position_data[3][1]],
#               [velocity_data[3][0]],[velocity_data[3][1]]])

# u = np.array([[acceleration_data[3][0]],
#               [acceleration_data[3][1]]])


## Step 0 - Initial State ##


## Previous State ##

## Step 1 - Predicted State ##

## Step 2 - Measurement from sensor ##

## Step 3 - Kalman Gain ##

## Step 4 - Update measurement & Kalman Gain ##