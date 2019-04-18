from line_follower_class import *


def go_back_to_blocks():

    lower_motor.on_for_degrees(30, -90)
    while right_side_sensor.reflected_light_intensity > 30:
        steer_pair.on(-100, -30)
    steer_pair.on_for_rotations(100, -20, 0.07)
    steer_pair.off()
    follow_for_xlines(2, right_side_sensor, speed=40, kp=0.2, ttarget=40)
    steer_pair.off()
    steer_pair.on_for_rotations(0, -35, 0.3)
    while right_side_sensor.reflected_light_intensity > 30:
        steer_pair.on(100, -20)
    steer_pair.on_for_rotations(-100, -20, 0.07)
    steer_pair.off()
    timed_follower(sensor=right_side_sensor, timemax=3.5, side_of_line=1, speed=60, kp=0.15, ttarget=50)
    follow_for_xlines(1, right_side_sensor, speed=40, kp=0.2, ttarget=40, side_of_line=1)
    steer_pair.off()


go_back_to_blocks()
