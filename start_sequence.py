#!/usr/bin/env python3
from sensor_and_motor_startup import *
from time import *

timelimit = time() + 10
sensor_declaration()
motor_initialization()
fourthblock = 0
count = 0


def start_sequence():
    global fourthblock, count
    lower_motor.off(brake=True)
    while side_color_sensor.value() == 0:
        hitechnic_pid_line_follower(sensor=right_side_sensor, speed=30, side=1)
    if not side_color_sensor.value() == 0 and count == 0:
        steer_pair.off()
        firstblock = side_color_sensor.value()
        print("Block 1: ", firstblock)
        sleep(4)
        steer_pair.on_for_rotations(0, -20, 0.2)
        steer_pair.off()
        secondblock = side_color_sensor.value()
        print("Block 2: ", secondblock)
        sleep(4)
        steer_pair.on_for_rotations(0, -20, 0.4)
        steer_pair.off()
        thirdblock = side_color_sensor.value()
        print("Block 3: ", thirdblock)
        sleep(4)
        steer_pair.on_for_rotations(0, -20, 0.3)
        steer_pair.off()
        fourthblock = side_color_sensor.value()
        print("Block 4: ", fourthblock)
        steer_pair.on_for_rotations(0, -20, 0.2)
        print("Block 1: ", firstblock)
        print("Block 2 : ", secondblock)
        print("Block 3 : ", thirdblock)
        print("Block 4 : ", fourthblock)
        count = count + 1

    steer_to_line(60, -60, center_sensor)
    steer_pair.off()
