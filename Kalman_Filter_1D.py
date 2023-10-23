from math_functions_1D import *

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
E_est = 2 #The inital error in estimate
E_mea = 4 #The error in measurement
previous_est = 68 # intial previous estimate
temperature_measurement = [75,71,70,74,70,75,71,76,74,74] # list of measurements
#####################################################################################


#####################################################################################
#################### THE KALMAN FILTER LOOP #########################################
#####################################################################################
for m in temperature_measurement:
    ### Calucaltion loop ###
    gain = kalman_gain(E_est,E_mea) #Kalman Gain
    crr_est = current_estimate(previous_est,m,gain) # Current estimate
    err_est = error_in_estimate(gain,E_est) #Error in current estimate
    
    ### Updation of variable ###
    E_est = err_est
    previous_est = crr_est

    ### Display loop ###
    print("   " + "Kalman Gain = " + str(gain) + 
          "||" + "Current Estimate = " + str(crr_est)+ 
          "||" + "Error in Estimate = " + str(err_est))
    print("=========================================================================")
######################################################################################

