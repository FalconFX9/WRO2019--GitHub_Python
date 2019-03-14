#!/usr/bin/env python3
from sensor_and_motor_startup import *

# Defining Sensors

sensor_declaration()
motor_initialization()

# SSH and on Brick Debugging

print('First Sensor Value')
for x in range(1, 50):
    print(left_side_sensor.value(0))
    sleep(0.1)

print('Second Sensor Value')
for x in range(1, 50):
    print(right_side_sensor.value(0))
    sleep(0.1)

"""
print('Third Sensor Value')
for x in range(1, 50):
    print(side_color_sensor.value(3))
    sleep(0.1)

print('Fourth Sensor Value')
for x in range(1, 50):
    print(center_sensor.reflected_light_intensity)
    sleep(0.1)
"""
