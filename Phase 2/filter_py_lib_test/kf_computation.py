'''
Module of Kalman filter computation

Author 
------
Gavin Furtado

AOCS Engineer
'''

import numpy as np

class kalman_initial(object):
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

    def P_initial(self,x_pos,y_pos,x_vel,y_vel):
        '''
        Needs verification

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
        
        pass

## Step 1 - Predicted State ##
class Prediction(object):
    def __init__(self, X_previous, P_previous, u, dt=2., w=0, Q=0) -> None:
        self.X_previous = X_previous
        self.u = u
        self.w = w
        self.dt = dt
        self.P_previous = P_previous
        self.Q = Q

    def A_matrix(self):
        # Computing Matrix A, B
        X_shape = self.X_previous.shape  #(4,1)

        if X_shape[0] == 4: 
            self.A = np.array([[1., 0., self.dt, 0.],
                               [0., 1., 0., self.dt],
                               [0., 0., 1., 0.],
                               [0., 0., 0., 1.]])
        elif X_shape[0] == 2:
            self.A = np.array([[1., self.dt],
                               [0., 1.]]) 
            
        elif X_shape[0] == 1:
            self.A = np.array([[1.]])

        else:
            print('Matrix A dimension does not match state matrix')

        return self.A

    def B_matrix(self):
        u_shape = self.u.shape # 2,1
        
        if u_shape[0] == 1: 
            self.B = np.array([[0.5*self.dt**2],
                               [self.dt**2]])

        elif u_shape[0] == 2:
            self.B = np.array([[0.5*self.dt**2, 0.],
                               [0., 0.5*self.dt**2],
                               [self.dt, 0.],
                               [0., self.dt]])
            
        else:
            print('Matrix B dimension does not match control matrix')

        return self.B

    def X_predicted(self):
        return (self.A_matrix()@self.X_previous) + (self.B_matrix()@self.u) #+ self.w 

    def P_predicted(self):
        pass

## Step 2 - Measurement from sensor ##



## Step 3 - Kalman Gain ##
class KalmanGain(object):
    def __init__(self)-> None:
        pass


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