
def kalman_gain(E_est,E_mea):
    gain = E_est/(E_est + E_mea)
    return  gain

# new branch testing
