#!/usr/bin/env python3
from ev3dev2.auto import *
from time import sleep
import time

# Time for while loops

close_time = time.time() + 5

# Defining the variables necessary to PID
# Target is the target value for the sensor (the one it gets when half of it is on the line and half of it is off)

Target = 50
Error = 0
Last_Error = 0
Integral = 0
Derivative = 0

Error2 = 0
Last_Error2 = 0
Integral2 = 0
Derivative2 = 0

motor_steering = 0

# PID Values --These are subjective and need to be tuned to the robot and mat
# Kp must be augmented or decreased until the robot follows the line smoothly --Higher Kp = Stronger corrections
# Same with Ki, after Kp is done --- note, Ki is not used in this case (error accumulation)
# Kd to 1, and move up or done until smooth, after Kp and Ki
# This process can take a VERY long time to fine-tune

Kp = 0.83
Ki = 0
Kd = 0.002

# To follow in a straight line -- Kp 0.085, Ki 0, Kd 0.005

Kp2 = 0.085
Ki2 = 0
Kd2 = 0.005

# Sensor declaration

Hitechnic1 = Sensor('in2:i2c1')
Hitechnic1.mode = 'RGB'
Hitechnic2 = Sensor('in3:i2c1')
Hitechnic2.mode = 'RGB'
Hitechnic3 = Sensor('in1:i2c1')
Hitechnic3.mode = 'RGB'
ColorRear = ColorSensor('in4')

# Motor Declaration

steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
grabber_servo = MediumMotor(OUTPUT_A)


# Function declaration --use these as much as possible


# PID Line Follower (1 sensor) --default : Hitechnic sensor in port 2, follows the line on the right side


def pidlinefollower(sensor=Hitechnic1, side=1):
    global Target, Error, Last_Error, Integral, Derivative, Kp, Ki, Kd, steer_pair, motor_steering
    Error = Target - (sensor.value(3) / 2)
    Integral = Error + Integral
    Derivative = Error - Last_Error
    motor_steering = ((Error * Kp) + (Integral * Ki) + (Derivative * Kd)) * side
    if ColorRear.reflected_light_intensity < 20:
        Kp = 0.43
    else:
        Kp = 0.83

    if Hitechnic3.value(3) < 20 and motor_steering < 0:
        steer_pair.on_for_seconds(40, -50, 1)

    print(ColorRear.reflected_light_intensity)
    steer_pair.on(motor_steering, -50)
    Last_Error = Error
    return


# PID Line Follower (2 sensors)


def doublepidlinefollower():
    global Error2, Last_Error2, Integral2, Derivative2, Kp2, Ki2, Kd2, steer_pair, motor_steering
    Error2 = (Hitechnic1.value(3) / 2) - (Hitechnic2.value(3) / 2)
    print(Hitechnic1.value(3), Hitechnic2.value(3))
    Integral2 = Error + Integral2
    Derivative2 = Error2 - Last_Error2
    motor_steering = ((Error2 * Kp2) + (Integral2 * Ki2) + (Derivative2 * Kd2))
    steer_pair.on(motor_steering, -60)
    Last_Error2 = Error2
    return


# Turn until line --default : Power set to -50, the amplitude and direction of the steering is set to 0


def steertoline(ampdir=0, power=-50):
    while not Hitechnic2.value(3) < 20:
        steer_pair.on(ampdir, power)
    steer_pair.off(brake=True)


# Lower the servo arm, go forward and raise the servo arm --default : Power set to 30
# Number of rotations of forward movement are 2


def lowerandpickup(power=30, rotations=2):
    if not grabber_servo.is_stalled():
        grabber_servo.on(-power)
    else:
        grabber_servo.off(brake=True)

    steer_pair.on_for_rotations(0, -30, rotations)

    if not grabber_servo.is_stalled():
        grabber_servo.on(power)
    else:
        grabber_servo.off(brake=True)


# Lower the servo arm, go backwards and raise the servo arm --default : Power is set to 30, Rotations is 2


def putdownobject(power=30, rotations=2):
    if not grabber_servo.is_stalled():
        grabber_servo.on(-power)
    else:
        grabber_servo.off(brake=True)

    steer_pair.on_for_rotations(0, 30, rotations)

    if not grabber_servo.is_stalled():
        grabber_servo.on(power)
    else:
        grabber_servo.off(brake=True)


# Start of the actual code



