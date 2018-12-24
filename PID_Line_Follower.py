from ev3dev2.auto import *
from time import sleep

# Defining the variables necessary to PID
# Target is the target value for the sensor (the one it gets when half of it is on the line and half of it is off)

Target = 46
Error = 0
Last_Error = 0
Integral = 0
Derivative = 0

# PID Values --These are subjective and need to be tuned to the robot and mat
# Kp must be augmented or decreased until the robot follows the line smoothly --Higher Kp = Stronger corrections
# Same with Ki, after Kp is done
# Kd to 1, and move up or done until smooth, after Kp and Ki
# This process can take a VERY long time to fine-tune

Kp = 0.5
Ki = 0
Kd = 0

# Sensor declaration

Hitechnic1 = Sensor('in2:i2c1')
Hitechnic1.mode = 'RGB'
Hitechnic2 = Sensor('in3:i2c1')
Hitechnic2.mode = 'RGB'

# Motor Declaration

steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)

# PID Line Follower (1 sensor)


def pidlinefollower(sensor=Hitechnic1, side=1):
    global Target, Error, Last_Error, Integral, Derivative, Kp, Ki, Kd, steer_pair
    Error = Target - (sensor.value(3)/2)
    Integral = Error + Integral
    Derivative = Error - Last_Error
    motor_steering = ((Error * Kp) + (Integral * Ki) + (Derivative * Kd)) * side
    steer_pair.on(motor_steering, -25)
    Last_Error = Error
    return


pidlinefollower(Hitechnic1, 1)
sleep(10)
steer_pair.off(brake=True)



