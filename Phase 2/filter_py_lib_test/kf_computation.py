'''
Module of Kalman filter computation

Author 
------
Gavin Furtado

AOCS Engineer
'''

import numpy as np
from constants import dt

## Test phase ##
class Test(object):
    def __init__(self, position, velocity, acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def loop(self):
        for _ in self.position:
            print(_)

def A_matrix(matrix):
    '''

    returns
    -------
    Matrix/array of size 1x1, 2x2, 4x4
    '''
    # Computing Matrix A, B
    mat_shape = matrix.shape  #(4,1)

    if mat_shape[0] == 4: 
        A = np.array([[1., 0., dt, 0.],
                      [0., 1., 0., dt],
                      [0., 0., 1., 0.],
                      [0., 0., 0., 1.]])
        
    elif mat_shape[0] == 2:
        A = np.array([[1., dt],
                      [0., 1.]]) 
        
    elif mat_shape[0] == 1:
        A = np.array([[1.]])

    else:
        raise ValueError('Matrix A dimension does not match state/process covariance matrix')

    return A      

def B_matrix(matrix):
    '''
    returns
    -------
    Matrix/array of size  2x2, 4x4
    '''
    mat_shape = matrix.shape # 2,1
    
    if mat_shape[0] == 1: 
        B = np.array([[0.5*dt**2],
                      [dt**2]])

    elif mat_shape[0] == 2:
        B = np.array([[0.5*dt**2, 0.],
                      [0., 0.5*dt**2],
                      [dt, 0.],
                      [0., dt]])
        
    else:
        raise ValueError('Matrix B dimension does not match control matrix')

    return B

class kalman_initial(object):
    '''
    Initalisition of parameters required in Kalman filter algorithm.

    Attributes
    ----------
    position : An array of 2-Dimensional array of x & y position coordinates
    velocity : An array of 2-Dimensional array of x & y velocities
    acceleration : An array of 2-Dimensional array of x & y acceleration

    Methods
    -------
    X_initial : Not required anymore 
    u_initial : Not required anymore
    P_initial : 
    '''
    def __init__(self,position, velocity, acceleration) -> None:
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def X_initial(self):
        return np.array([[self.position[0][0]], [self.position[0][1]],
                         [self.velocity[0][0]], [self.velocity[0][1]]])

    def u_initial(self):
        return np.array([[self.acceleration[0][0]],
                         [self.acceleration[0][1]]])

    def P_initial(self,x_pos_err,y_pos_err,x_vel_err,y_vel_err):
        '''
        Needs verification but mostly feels right
        Compute the initial process covariance matrix

        Attributes
        ----------
        x_pos : x-position process error
        y_pos : y-position process error
        x_vel : x-velocity process error
        y_vel : y-velocity process error

        Matrix
        ------
        np.array([[x-position-process-error**2,0,0,0],
                  [0,y-position-process-error**2,0,0],
                  [0,0,x-velocity-process-error**2,0],
                  [0,0,0,y-velocity-process-error**2]])
        '''
        P = np.array([[x_pos_err**2,0,0,0],
                      [0,y_pos_err**2,0,0],
                      [0,0,x_vel_err**2,0],
                      [0,0,0,y_vel_err**2]])
        return P

## Step 1 - Predicted State ##
class Prediction(object):
    def __init__(self, X_previous, P_previous, u, dt=dt, w=0, Q=0) -> None:
        self.X_previous = X_previous
        self.u = u
        self.w = w
        self.dt = dt
        self.P_previous = P_previous
        self.Q = Q

    def X_predicted(self):
        # return (self.A_matrix()@self.X_previous) + (self.B_matrix()@self.u) #+ self.w 
        return (A_matrix(self.X_previous)@self.X_previous) + (B_matrix(self.u)@self.u) #+ self.w 

    def P_predicted(self):
        '''
        A.P_prev.A^T + Q
        '''
        prev = self.P_previous
        P = A_matrix(prev)@prev@(A_matrix(prev).transpose()) #+Q
        
        ## Simplyfing the calcuations
        P[0][1] = 0 
        P[0][2] = 0
        P[0][1] = 0
        P[1][0] = 0
        P[1][2] = 0
        P[1][3] = 0
        P[2][0] = 0
        P[2][1] = 0
        P[2][3] = 0
        P[3][0] = 0
        P[3][1] = 0
        P[3][2] = 0

        return P 

## Step 2 - Measurement from sensor ##



## Step 3 - Kalman Gain ##
def H_matrix():
    '''
    Transformation matrix for easy of multiplication.
    In this case it is 4x4 identity matrix
    '''
    return np.array([[1,0,0,0],
                      [0,1,0,0],
                      [0,0,1,0],
                      [0,0,0,1],])

def R_matrix(x_pos_obs_err,y_pos_obs_err,x_vel_obs_err,y_vel_obs_err):
    '''
    Observation error matrix

    Attributes
    ----------
    x_pos : x-position observation error
    y_pos : y-position observation error
    x_vel : x-velocity observation error
    y_vel : y-velocity observation error

    Matrix
    ------
    np.array([[x-position-observation-error**2,0,0,0],
              [0,y-position-observation-error**2,0,0],
              [0,0,x-velocity-observation-error**2,0],
              [0,0,0,y-velocity-observation-error**2]])
    '''
    R = np.array([[x_pos_obs_err**2,0,0,0],
                    [0,y_pos_obs_err**2,0,0],
                    [0,0,x_vel_obs_err**2,0],
                    [0,0,0,y_vel_obs_err**2]])
    return R


def KalmanGain(P, R):
    '''
    K = P_predict . H^T / (H.P_predict.H^T  + R)
    '''
    numerator = P@H_matrix().transpose()
    denominator = H_matrix()@P@H_matrix().transpose() + R
    k = numerator @ np.linalg.inv(denominator)
    return k

## Step 4 - Measurement input
def measurement_input():
    '''
    Y = C.X + Z
    '''
    C = np.array([[1,0,0,0],
                  [0,1,0,0],
                  [0,0,1,0],
                  [0,0,0,1],])
    
    return 

## Step 4 - Update measurement & Kalman Gain ##
class updation(object):
    def __init__(self) -> None:
        pass

    def C_matrix(self,Y):
        pass

    def measurement(self):
        # CYm + zk
        pass

    def P_updated(self):
        pass

    def X_updated(self):
        pass