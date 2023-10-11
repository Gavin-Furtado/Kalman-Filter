## This script consists of all the mathematical formulae 
## required for Kalman filter calculations


def kalman_gain(E_est,E_mea):
    gain = E_est/(E_est + E_mea)
    return  gain


