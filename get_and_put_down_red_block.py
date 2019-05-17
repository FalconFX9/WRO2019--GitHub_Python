from pick_up_first_block import *


def go_back_to_pickup():
    left_side_sensor.mode = 'COL-REFLECT'
    while right_side_sensor.reflected_light_intensity > 30:
        steer_pair.on(-100, -30)
    steer_pair.on_for_rotations(100, -20, 0.07)
    steer_pair.off()
    grabber_servo.on_for_degrees(30, 180)
    follow_for_xlines(1, right_side_sensor, speed=40, kp=0.2, ttarget=40)
    steer_pair.off()
    steer_pair.on_for_rotations(0, -35, 0.3)
    while left_side_sensor.reflected_light_intensity > 30:
        steer_pair.on(-100, -20)
    steer_pair.off()
    follow_to_line(left_side_sensor, side_of_line=1, kp=0.3)
    steer_pair.off()
    turn_right(left_side_sensor)


go_back_to_pickup()
