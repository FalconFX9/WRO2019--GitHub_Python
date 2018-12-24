from ev3dev2.auto import *
from time import sleep
import time

# Time for while loops

close_time = time.time()+5

# Defining the variables necessary to PID
# Target is the target value for the sensor (the one it gets when half of it is on the line and half of it is off)

Target = 28
Error = 0
Last_Error = 0
Integral = 0
Derivative = 0

Error2 = 0
Last_Error2 = 0
Integral2 = 0
Derivative2 = 0

# PID Values --These are subjective and need to be tuned to the robot and mat
# Kp must be augmented or decreased until the robot follows the line smoothly --Higher Kp = Stronger corrections
# Same with Ki, after Kp is done --- note, Ki is not used in this case (error accumulation)
# Kd to 1, and move up or done until smooth, after Kp and Ki
# This process can take a VERY long time to fine-tune

Kp = 0.43
Ki = 0
Kd = 0.002

Kp2 = 0.3
Ki2 = 0
Kd2 = 0.002

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
    print(sensor.value(3))
    Integral = Error + Integral
    Derivative = Error - Last_Error
    motor_steering = ((Error * Kp) + (Integral * Ki) + (Derivative * Kd)) * side
    steer_pair.on(motor_steering, -85)
    Last_Error = Error
    return


def doublepidlinefollower():
    global Error2, Last_Error2, Integral2, Derivative2, Kp2, Ki2, Kd2, steer_pair
    Error2 = (Hitechnic1.value(3)/2) - (Hitechnic2.value(3) / 2)
    print(Hitechnic1.value(3), Hitechnic2.value(3))
    Integral2 = Error + Integral2
    Derivative2 = Error2 - Last_Error2
    motor_steering = ((Error2 * Kp2) + (Integral2 * Ki2) + (Derivative2 * Kd2))
    steer_pair.on(motor_steering, -85)
    Last_Error2 = Error2
    return


while time.time() < close_time:
        doublepidlinefollower()

steer_pair.off(brake=True)
