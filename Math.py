## This script consists of all the mathematical formulae 
## required for Kalman filter calculations

## Math equation ##
## KG = Eest / (Eest + Emea) ##
def kalman_gain(E_est:float,E_mea:float)->float:
    '''This function calculates the Kalman gain
    input: Error in estimate, Error in measurement
    output: Kalman gain
    '''
    gain = E_est/(E_est + E_mea)
    return  round(gain,2)

## Math equation ##
## Current Estimate = Previous extimate + KG[measurement - previous estimate] ##
def current_estimate(previous_est:float,
                      measurement:float,
                      kalmangain:float)->float:
   '''
   This function calcuates the current esitmate for the kalman filter
   input: previous estimate, currrent measurement, kalman gain
   output: current estimate
   '''
   residual = measurement - previous_est
   weighted_residue = kalmangain * residual 
   return round((previous_est + weighted_residue),2)

## Math equation ##
## Error in current estimate = [1 - KG] x error in previous estimate ##
def error_in_estimate(kalmangain:float,error_previous_est:float)->float:
    '''
    Calulates the error in current estimate
    input: Kalman Gain, Error in previous estimate
    output: Error in current estimate
    '''
    return round((1-kalmangain)*error_previous_est,2)

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