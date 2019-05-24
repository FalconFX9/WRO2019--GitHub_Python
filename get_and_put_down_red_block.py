# from pick_up_first_block import blocks
from line_follower_class import *


blocks = ['black', 'white', 'black']
def go_back_to_pickup():
    left_side_sensor.mode = 'COL-REFLECT'
    while right_side_sensor.reflected_light_intensity > 30:
        steer_pair.on(-100, -30)
    steer_pair.on_for_rotations(100, -20, 0.07)
    steer_pair.off()
    follow_for_xlines(1, right_side_sensor, speed=40, kp=0.2, ttarget=40)
    steer_pair.off()
    steer_pair.on_for_rotations(0, -35, 0.3)
    while left_side_sensor.reflected_light_intensity > 30:
        steer_pair.on(-100, -20)
    steer_pair.off()
    follow_to_line(left_side_sensor, side_of_line=1, kp=0.4)
    steer_pair.off()
    steer_pair.on_for_rotations(0, -40, 0.15)
    turn_right(left_side_sensor)
    if blocks[2] == 'black':
        follow_for_xlines(2, left_side_sensor, 1)
    elif blocks[1] == 'black':
        follow_for_xlines(3, left_side_sensor, 1)
    steer_pair.off()
    lower_motor.on_for_degrees(10, -10)
    steer_pair.on_for_rotations(-60, 40, 1.2)
    while center_sensor.reflected_light_intensity > 30:
        steer_pair.on(-60, 15)
    steer_pair.off()
    steer_pair.on_for_rotations(0, 20, 0.2)
    lower_motor.on_for_degrees(20, 58)
    sleep(0.6)
    timed_follower(sensor=center_sensor, timemax=0.45, speed=40, kp=0.25, ttarget=30)
    steer_pair.off()
    lower_motor.on_for_degrees(10, -52)
    steer_pair.on_for_rotations(0, -40, 0.2)
    steer_pair.on_for_rotations(70, 40, 0.7)
    while left_side_sensor.reflected_light_intensity > 30:
        steer_pair.on(70, 30)
    steer_pair.off()
    if blocks[2] == 'black':
        follow_for_xlines(3, left_side_sensor, 1)
    elif blocks[1] == 'black':
        follow_for_xlines(2, left_side_sensor, 1)
    steer_pair.off()
    steer_pair.on_for_rotations(0, -40, 0.4)
    turn_right(center_sensor)
    follow_for_xlines(4, center_sensor, 1, line_sensor=right_side_sensor)
    steer_pair.off()
    steer_pair.on_for_rotations(0, -40, 0.67)
    steer_pair.on_for_rotations(72, 40, 0.9)
    while center_sensor.reflected_light_intensity > 30:
        steer_pair.on(70, 20)
    steer_pair.off()
    steer_pair.on_for_rotations(0, 40, 0.6)


go_back_to_pickup()
lower_motor.off(False)
grabber_servo.off(False)
