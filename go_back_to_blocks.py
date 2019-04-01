from line_follower_class import *
from threading import *


def go_back_to_blocks():
    global lines_passed
    while right_side_sensor.reflected_light_intensity > 30:
        steer_pair.on(-100, -30)
    steer_pair.on_for_rotations(100, -20, 0.07)
    steer_pair.off()
    t = Thread(target=check_for_lines, args=(2,))
    t.start()
    while not lines_passed:
        losp_right_follower(speed=30)
    lines_passed = False
    steer_pair.off()
    steer_pair.on_for_rotations(0, -35, 0.3)
    while right_side_sensor.reflected_light_intensity > 30:
        steer_pair.on(100, -20)
    steer_pair.on_for_rotations(-100, -20, 0.07)
    steer_pair.off()
    timed_follower(sensor=right_side_sensor, timemax=3.5, side_of_line=1, speed=60, kp=0.15, ttarget=50)
    t = Thread(target=check_for_lines, args=(1,))
    t.start()
    while not lines_passed:
        hisp_right_follower(side_of_line=1, speed=30)
    steer_pair.off()
    lines_passed = False


go_back_to_blocks()
