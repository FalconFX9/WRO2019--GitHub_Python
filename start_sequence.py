#!/usr/bin/env python3
from line_follower_class import *
from time import *
from threading import *

timelimit = time() + 10
motor_initialization()
colorblock = []


def start_sequence():
    def play_soviet_anthem():
        sound = Sound()
        sound.play('/home/robot/Sounds/soviet-anthem.wav')

    def see_color_blocks():
        while len(colorblock) < 4:
            if not (side_color_sensor.value() == 17 or side_color_sensor.value() == 0):
                colorblock.append(side_color_sensor.value())
                sleep(0.3)
    global colorblock
    print('Start Sequence')
    grabber_servo.on_for_degrees(speed=50, degrees=-180)
    lower_motor.on_for_degrees(speed=60, degrees=-90)
    steer_pair.on_for_rotations(35, -40, 0.4)
    lower_motor.off(brake=True)
    while side_color_sensor.value() == 17 or side_color_sensor.value() == 0:
        losp_right_follower(speed=45)
    t = Thread(target=see_color_blocks)
    t.start()
    while not len(colorblock) == 4:
        hisp_right_follower(speed=40)
    print(colorblock)
    follow_to_line(following_sensor=right_side_sensor, speed=40)
    steer_pair.off()
    steer_pair.on_for_rotations(0, -35, 0.3)
    while right_side_sensor.reflected_light_intensity > 30:
        steer_pair.on(100, -30)
    steer_pair.on_for_rotations(-100, -20, 0.04)
    steer_pair.off()

