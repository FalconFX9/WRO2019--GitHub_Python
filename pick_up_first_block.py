from line_follower_class import *
from threading import Thread

side_color_sensor.mode = 'RGB'
block_is_black = False


def look_at_blocks():
    global block_is_black
    while not block_is_black:
        if side_color_sensor.value(3) > 100:
            sleep(0.3)
        elif 100 > side_color_sensor.value(3) > 40:
            block_is_black = True
    print('Thread look_at_blocks is finished')


def pick_up_block():
    global block_is_black
    lower_motor.off()
    while not block_is_black:
        hisp_right_follower(speed=40, kp=0.15)
        print(side_color_sensor.value(3))
    steer_pair.off()
    follow_to_line(right_side_sensor, center_sensor, 30, kp=0.2)
    steer_pair.off()
    steer_pair.on_for_rotations(0, 30, 0.3)
    lower_motor.on_for_degrees(10, -10)
    steer_pair.on_for_rotations(60, 40, 1.2)
    steer_pair.on_for_rotations(0, 20, 0.2)
    lower_motor.on_for_degrees(10, 56)
    sleep(0.2)
    timed_follower(sensor=center_sensor, timemax=0.85, speed=20, kp=0.35)
    steer_pair.off()
    lower_motor.on_for_degrees(10, -52)


Thread(target=look_at_blocks).start()
pick_up_block()
