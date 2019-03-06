#!/usr/bin/env python3
from ev3dev2.auto import *
from time import *

# Defining the variables necessary to PID
# Target is the target value for the sensor (the one it gets when half of it is on the line and half of it is off)
# works well at target 35
target = 35
error = 0
last_error = 0
integral = 0
derivative = 0

starget = 24
error2 = 0
last_error2 = 0
integral2 = 0
derivative2 = 0

motor_steering2 = 0

# PID Values --These are subjective and need to be tuned to the robot and mat
# Kp must be augmented or decreased until the robot follows the line smoothly --Higher Kp = Stronger corrections
# Same with Ki, after Kp is done --- note, Ki is not used in this case (error accumulation)
# Kd to 1, and move up or done until smooth, after Kp and Ki
# This process can take a VERY long time to fine-tune
Kp = 0.3
Ki = 0
Kd = 0

Skp = 0.3
Ski = 0
Skd = 0
# To follow in a straight line -- Kp 0.085, Ki 0, Kd 0.005
Kp2 = 0.085
Ki2 = 0
Kd2 = 0.005

# Sensor declaration
hitechnic_1 = None
line_1 = ColorSensor('in2')
side_color_sensor = None
line_2 = None
not_connected = False


def sensor_declaration():
    global hitechnic_1, line_1, side_color_sensor, line_2, not_connected
   # hitechnic_1 = Sensor('in1:i2c1')
   # hitechnic_1.mode = 'RGB'
    line_1 = ColorSensor('in2')
    side_color_sensor = Sensor('in3')
    side_color_sensor.mode = 'COLOR'
   # line_2 = ColorSensor('in4')


# Motor Declaration
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
grabber_servo = MediumMotor(OUTPUT_A)
lower_motor = LargeMotor(OUTPUT_D)


def motor_initialization():
    global steer_pair, grabber_servo, not_connected
    try:
        steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
    except DeviceNotFound:
        print('Main motors not found')
        not_connected = True

    try:
        grabber_servo = MediumMotor(OUTPUT_A)
    except DeviceNotFound:
        print('Main servo not found')
        not_connected = True


# Function declaration --use these as much as possible

sensor_declaration()
motor_initialization()


# PID Line Follower (1 sensor) --default : Hitechnic sensor in port 1, follows the line on the right side
def hitechnic_pid_line_follower(sensor=hitechnic_1, side=1, speed=60):
    global target, error, last_error, integral, derivative, Kp, Ki, Kd, steer_pair, motor_steering2
    error = target - (sensor.value(3) / 2)
    integral = error + integral
    derivative = error - last_error
    motor_steering2 = ((error * Kp) + (integral * Ki) + (derivative * Kd)) * side
    steer_pair.on(motor_steering2, -speed)
    last_error = error


def stock_pid_follower(sensor=line_1, side=1, speed=60, corretion='L'):
    global starget, error2, last_error2, integral2, derivative2, Skp, Ski, Skd, steer_pair, motor_steering2
    if corretion == 'H':
        Skp = 0.1
        Ski = 0
        Skd = 0
    error2 = starget - sensor.reflected_light_intensity
    print(sensor.reflected_light_intensity)
    integral2 = error2 + integral2
    derivative2 = error2 - last_error2
    motor_steering2 = ((error2 * Skp) + (integral2 * Ski) + (derivative2 * Skd)) * side
    steer_pair.on(motor_steering2, -speed)
    last_error2 = error2


# PID Line Follower (2 sensors)
def double_pid_line_follower(speed=60):
    global error2, last_error2, integral2, derivative2, Kp2, Ki2, Kd2, steer_pair, motor_steering
    error2 = line_1.reflected_light_intensity - line_2.reflected_light_intensity
    integral2 = error + integral2
    derivative2 = error2 - last_error2
    motor_steering = ((error2 * Kp2) + (integral2 * Ki2) + (derivative2 * Kd2))
    steer_pair.on(motor_steering, -speed)
    last_error2 = error2


# Turn until line --default : Power set to -50, the amplitude and direction of the steering is set to 0
def steer_to_line(turn_tightness=0, power=-50, sensor=line_1):
    while not sensor.color == 1:
        steer_pair.on(turn_tightness, power)
    steer_pair.off(brake=True)


# Lower the servo arm, go forward and raise the servo arm --default : Power set to 30
# Number of rotations of forward movement are 2
def lower_and_pickup(power=30, degrees=30):
    lower_motor.on_for_degrees(speed=power, degrees=degrees)
    steer_pair.on_for_degrees(0, -30, 30)


# Lower the servo arm, go backwards and raise the servo arm --default : Power is set to 30, Rotations is 2
def put_down_object(power=30, degrees=30):
    lower_motor.on_for_degrees(speed=power, degrees=degrees)
    steer_pair.on_for_degrees(0, 30, 40)


# Start of the actual code
"""
def wro2018():

    if not_connected:
        for x in range(1, 5):
            sound = Sound()
            sound.beep()
            sleep(0.2)
            quit()
    else:
        grabber_servo.on_for_rotations(-100, 7)

        while side_color_sensor.value() == 0:
            pid_line_follower(hitechnic_1, 1, 20)
            print(side_color_sensor.value())

        steer_pair.off()

        grabber_servo.on_for_rotations(speed=100, rotations=6)

        pid_line_follower(hitechnic_1, 1, 20)
        sleep(0.5)
        steer_pair.off()

        grabber_servo.on_for_rotations(-100, 7)

        while not side_color_sensor.value() == 0:
            pid_line_follower(hitechnic_1, 1, 20)

        while not side_color_sensor.value() == 4:
            pid_line_follower(hitechnic_1, 1, 20)
            print(side_color_sensor.value())

        steer_pair.off()

        grabber_servo.on_for_rotations(speed=100, rotations=6)
        steer_pair.on_for_rotations(0, 20, 2)

        steer_pair.off(brake=False)
        grabber_servo.off(brake=False)
"""
