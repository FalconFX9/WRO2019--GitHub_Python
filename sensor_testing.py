#!/usr/bin/env python3
from ev3dev2.auto import *
from time import sleep
from PID_Line_Follower import *

time_duration = time.time() + 5


# Defining Sensors

sensor_declaration()
motor_initialization()
# Sensor1 = Sensor('in1')
# Sensor2 = Sensor('in1')
# Sensor3 = Sensor('in3')
# Sensor4 = ColorSensor('in4')

# Setting Sensor mode

# Sensor1.mode = 'RGB'
# Sensor2.mode = 'RGB'
# Sensor3.mode = 'RGB'

# SSH and on Brick Debugging

grabber_servo.on_for_rotations(-100, 10)
if grabber_servo.is_stalled:
    grabber_servo.off(brake=True)
    sleep(5)
grabber_servo.on_for_rotations(100, 11)
if grabber_servo.is_stalled:
    grabber_servo.off(brake=True)

print('First Sensor Value')
for x in range(1, 50):
    print(hitechnic_1.value(3))
    sleep(0.1)

print('Second Sensor Value')
for x in range(1, 50):
    print(hitechnic_2.value(3))
    sleep(0.1)

print('Third Sensor Value')
for x in range(1, 50):
    print(side_color_sensor.value(3))
    sleep(0.1)

print('Fourth Sensor Value')
for x in range(1, 50):
    print(color_rear.reflected_light_intensity)
    sleep(0.1)
