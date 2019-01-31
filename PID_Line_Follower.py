#!/usr/bin/env python3
from ev3dev2.auto import *
import time

timelimit = time.time() + 10
# Defining the variables necessary to PID
# Target is the target value for the sensor (the one it gets when half of it is on the line and half of it is off)
# works well at target 35
target = 35
error = 0
last_error = 0
integral = 0
derivative = 0

error2 = 0
last_error2 = 0
integral2 = 0
derivative2 = 0

motor_steering = 0

# PID Values --These are subjective and need to be tuned to the robot and mat
# Kp must be augmented or decreased until the robot follows the line smoothly --Higher Kp = Stronger corrections
# Same with Ki, after Kp is done --- note, Ki is not used in this case (error accumulation)
# Kd to 1, and move up or done until smooth, after Kp and Ki
# This process can take a VERY long time to fine-tune
Kp = 0.2
Ki = 0
Kd = 0

# To follow in a straight line -- Kp 0.085, Ki 0, Kd 0.005
Kp2 = 0.085
Ki2 = 0
Kd2 = 0.005

# Sensor declaration
hitechnic_1 = 'null'
hitechnic_2 = 'null'
side_color_sensor = 'null'
colorRear = 'null'

try:
    hitechnic_1 = Sensor('in1:i2c1')
except DeviceNotFound:
    print('Sensor 1 not found')
else:
    hitechnic_1.mode = 'RGB'

try:
    hitechnic_2 = Sensor('in2:i2c1')
except DeviceNotFound:
    print('Sensor 2 not found')
else:
    hitechnic_2.mode = 'RGB'

try:
    side_color_sensor = Sensor('in3:i2c1')
except DeviceNotFound:
    print('Sensor 3 not found')

try:
    colorRear = ColorSensor('in4')
except DeviceNotFound:
    print('Sensor 4 not found')

side_color_sensor.mode = 'Color'

# Motor Declaration
steer_pair = 'null'
try:
    steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
except DeviceNotFound:
    print('Main motors not found')

grabber_servo = 'null'
try:
    grabber_servo = MediumMotor(OUTPUT_A)
except DeviceNotFound:
    print('Main servo not found')

# Function declaration --use these as much as possible


# PID Line Follower (1 sensor) --default : Hitechnic sensor in port 1, follows the line on the right side
def pid_line_follower(sensor=hitechnic_1, side=1):
    global target, error, last_error, integral, derivative, Kp, Ki, Kd, steer_pair, motor_steering
    error = target - (sensor.value(3) / 2)
    integral = error + integral
    derivative = error - last_error
    motor_steering = ((error * Kp) + (integral * Ki) + (derivative * Kd)) * side
    print(hitechnic_1.value(3))
    steer_pair.on(motor_steering, -40)
    last_error = error

# PID Line Follower (2 sensors)
def double_pid_line_follower():
    global error2, last_error2, integral2, derivative2, Kp2, Ki2, Kd2, steer_pair, motor_steering
    error2 = (hitechnic_1.value(3) / 2) - (hitechnic_2.value(3) / 2)
    print(hitechnic_1.value(3), hitechnic_2.value(3))
    integral2 = error + integral2
    derivative2 = error2 - last_error2
    motor_steering = ((error2 * Kp2) + (integral2 * Ki2) + (derivative2 * Kd2))
    steer_pair.on(motor_steering, -60)
    last_error2 = error2


# Turn until line --default : Power set to -50, the amplitude and direction of the steering is set to 0
def steer_to_line(turn_tightness=0, power=-50):
    while not hitechnic_2.value(3) < 20:
        steer_pair.on(turn_tightness, power)
    steer_pair.off(brake=True)


# Lower the servo arm, go forward and raise the servo arm --default : Power set to 30
# Number of rotations of forward movement are 2
def lower_and_pickup(power=30, rotations=2):
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
def put_down_object(power=30, rotations=2):
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
while not side_color_sensor.value() == 7 or side_color_sensor.value() == 6:
    pid_line_follower(hitechnic_1, 1)

steer_pair.off()
