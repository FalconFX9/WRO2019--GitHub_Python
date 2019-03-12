#!/usr/bin/env python3
from line_follower_class import *
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
        losp_right_follower(side_of_line=1)
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

    follow_to_line(following_sensor=right_side_sensor, side_of_line=1)
    steer_pair.off()


start_sequence()
