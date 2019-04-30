from line_follower_class import *

side_color_sensor.mode = 'RGB'


def pick_up_block():
    while not 100 > side_color_sensor.value(3) > 40:
        hisp_right_follower(40, 0.15)
    steer_pair.off()
    steer_pair.on_for_rotations(0, -30, 0.1)
    follow_to_line(following_sensor=right_side_sensor, line_sensor=center_sensor, speed=30, kp=0.1)
    lower_motor.on_for_degrees(10, -10)
    steer_pair.on_for_rotations(0, 30, 0.15)
    steer_pair.on_for_rotations(60, 40, 1.14)
    steer_pair.on_for_rotations(0, 20, 0.2)
    lower_motor.on_for_degrees(10, 50)
    timed_follower(sensor=center_sensor, timemax=0.65, speed=20, kp=0.35, side_of_line=1)
    steer_pair.off()
    lower_motor.on_for_degrees(10, -52)
