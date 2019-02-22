#!/usr/bin/env python3
from sensor_and_motor_startup import *
from time import *

timelimit = time() + 10
sensor_declaration()
motor_initialization()
fourthblock = 0


def start_sequence():
    global fourthblock
    lower_motor.off(brake=True)
    while fourthblock == 0:
        stock_pid_follower(sensor=line_1, speed=30, side=1)
        if not side_color_sensor.value() == 0:
            steer_pair.off()
            firstblock = side_color_sensor.value()
            steer_pair.on_for_rotations(0, -20, 0.2)
            print(firstblock)
            if not side_color_sensor.value() == 0:
                steer_pair.off()
                secondblock = side_color_sensor.value()
                steer_pair.on_for_rotations(0, -20, 0.2)
                print(secondblock)
                if not side_color_sensor.value() == 0:
                    steer_pair.off()
                    thirdblock = side_color_sensor.value()
                    steer_pair.on_for_rotations(0, -20, 0.2)
                    print(thirdblock)
                    if not side_color_sensor.value() == 0:
                        steer_pair.off()
                        fourthblock = side_color_sensor.value()
                        steer_pair.on_for_rotations(0, -20, 0.2)
                        print(firstblock)
                        print(secondblock)
                        print(thirdblock)
                        print(fourthblock)

    steer_to_line(100, -60, line_1)
    steer_pair.off()
