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
    return  gain

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
   return (previous_est + weighted_residue)

## Math equation ##
## Error in current estimate = [1 - KG] x error in previous estimate ##
def error_in_estimate(kalmangain:float,error_previous_est:float)->float:
    '''
    Calulates the error in current estimate
    input: Kalman Gain, Error in previous estimate
    output: Error in current estimate
    '''
    return (1-kalmangain)*error_previous_est


gain = kalman_gain(4,6)
print("Kalman gain=" +str(gain))