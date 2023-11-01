'''
This module performs the computation of the 
Kalman filter for one variable, such as the
temperature

Author: Gavin Furtado

Reference: Michel Van Biezen lectures
'''

from math_functions import kalman_gain, current_estimate, error_in_estimate

#########################################################
### Solving a one dimensional temperature example
### True temperature = 72
### Initial estimate = 68
### Initial error in estimate = 2
### Inital measurement = 75
### Error in measurement = 4  
#########################################################

#####################################################################################
### Inital variables ###
ERROR_IN_EST = 2 #The inital error in estimate
ERROR_IN_MEA = 4 #The error in measurement
PREVIOUS_EST = 68 # intial previous estimate
temperature_measurement = [75,71,70,74,70,75,71,76,74,74] # list of measurements
#####################################################################################


#################### THE KALMAN FILTER LOOP #########################################
#####################################################################################
for m in temperature_measurement:
    ### Calucaltion loop ###
    gain = kalman_gain(ERROR_IN_EST,ERROR_IN_MEA) #Kalman Gain
    crr_est = current_estimate(PREVIOUS_EST,m,gain) # Current estimate
    err_est = error_in_estimate(gain,ERROR_IN_EST) #Error in current estimate
    
    ### Updation of variable ###
    ERROR_IN_EST = err_est
    PREVIOUS_EST = crr_est

    ### Display loop ###
    print("   " + "Kalman Gain = " + str(gain) + 
          "||" + "Current Estimate = " + str(crr_est)+ 
          "||" + "Error in Estimate = " + str(err_est))
    print("=========================================================================")
######################################################################################

