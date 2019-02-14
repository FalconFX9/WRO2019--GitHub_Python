#!/usr/bin/env python3
from sensor_and_motor_startup import *
from line_follower_class import *
from time import *

sensor_declaration()
motor_initialization()


def start_sequence():
    follower = OneSensorLineFollower(side_color_sensor, steer_pair)
    while time.time() > time.time() + 10:
        follower.follower()
        if not side_color_sensor.value() == 0:
            firstblock = side_color_sensor.value()
            if not side_color_sensor.value() == 0 or side_color_sensor.value() == firstblock:
                secondblock = side_color_sensor.value()
                if not side_color_sensor.value() == 0 or side_color_sensor.value() == firstblock or \
                        side_color_sensor.value() == secondblock:
                    thirdblock = side_color_sensor.value()
                    if not side_color_sensor.value() == 0 or side_color_sensor.value() == firstblock or \
                            side_color_sensor.value() == secondblock or side_color_sensor.value() == thirdblock:
                        fourthblock = side_color_sensor.value()
                        print(firstblock)
                        print(secondblock)
                        print(thirdblock)
                        print(fourthblock)

    steer_to_line(100, -60, hitechnic_1)
