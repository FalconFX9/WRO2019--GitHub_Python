from line_follower_class import *

side_color_sensor.mode = 'RGB'


def pick_up_block():
    lower_motor.off()
    while not 100 > side_color_sensor.value(3) > 40:
        hisp_right_follower(speed=40, kp=0.15)
    steer_pair.off()
    steer_pair.on_for_rotations(0, -30, 0.1)
    timed_follower(sensor=right_side_sensor, speed=30, kp=0.15, timemax=0.33)
    lower_motor.on_for_degrees(10, -10)
    steer_pair.on_for_rotations(60, 40, 1.2)
    steer_pair.on_for_rotations(0, 20, 0.2)
    lower_motor.on_for_degrees(10, 56)
    timed_follower(sensor=center_sensor, timemax=0.85, speed=20, kp=0.35, side_of_line=1)
    steer_pair.off()
    lower_motor.on_for_degrees(10, -52)


pick_up_block()
