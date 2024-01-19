import sensor as sn


## Sensor Data
sensor = sn.PositionSensor(noise_mean=0.2, noise_std=1.5, dt=1,sample_size=50)
position, velocity, acceleration, noise = sensor.data_set()

print(position)

## Step 0 - Initial State ##


## Previous State ##

## Step 1 - Predicted State ##

## Step 2 - Measurement from sensor ##

## Step 3 - Kalman Gain ##

## Step 4 - Update measurement & Kalman Gain ##