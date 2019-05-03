from line_follower_class import *
from threading import Thread

side_color_sensor.mode = 'RGB'
block_is_black = False
t_time = 0


def look_at_blocks():
    global block_is_black
    while not block_is_black:
        if side_color_sensor.value(3) > 100:
            sleep(0.3)
        elif 100 > side_color_sensor.value(3) > 40:
            block_is_black = True
    print('Thread look_at_blocks is finished')


def pick_up_block():
    global block_is_black, t_time
    lower_motor.off()
    start_time = time()
    while not block_is_black:
        hisp_right_follower(speed=40, kp=0.15)
    steer_pair.off()
    t_time = time() - start_time
    steer_pair.on_for_rotations(0, -30, 0.1)
    follow_to_line(right_side_sensor, center_sensor, 30, kp=0.2)
    steer_pair.off()
    lower_motor.on_for_degrees(10, -10)
    steer_pair.on_for_rotations(60, 40, 1.2)
    steer_pair.on_for_rotations(0, 20, 0.2)
    lower_motor.on_for_degrees(20, 56)
    sleep(0.6)
    timed_follower(sensor=center_sensor, timemax=0.35, speed=40, kp=0.35)
    steer_pair.off()
    lower_motor.on_for_degrees(10, -52)


def go_to_put_down():
    global t_time
    steer_pair.on_for_rotations(0, -40, 0.3)
    steer_pair.on_for_rotations(-70, 40, 0.7)
    while right_side_sensor.reflected_light_intensity > 30:
        steer_pair.on(-70, 30)
    steer_pair.off()
    if t_time < 1:
        follow_for_xlines(3, sensor=right_side_sensor, speed=50, ttarget=45, kp=0.2)
        steer_pair.off()
    else:
        follow_for_xlines(2, sensor=right_side_sensor, speed=50, ttarget=45, kp=0.2)
        steer_pair.off()
    steer_pair.on_for_rotations(0, -40, 0.2)
    steer_pair.on_for_rotations(-70, 40, 0.7)
    while right_side_sensor.reflected_light_intensity > 30:
        steer_pair.on(-70, 30)
    steer_pair.off()
    steer_pair.on_for_rotations(-70, 40, 0.1)
    follow_to_line(following_sensor=right_side_sensor, line_sensor=center_sensor, speed=40, kp=0.65)
    steer_pair.off()
    steer_pair.on_for_rotations(0, -40, 0.65)
    steer_pair.on_for_rotations(-70, 40, 0.7)
    while center_sensor.reflected_light_intensity > 30:
        steer_pair.on(-70, 30)
    steer_pair.off()
    steer_pair.on_for_rotations(70, 40, 0.05)
    follow_to_line(following_sensor=center_sensor, line_sensor=right_side_sensor, side_of_line=1, speed=30, kp=0.4)
    steer_pair.off()
    steer_pair.on_for_rotations(0, -40, 0.65)
    steer_pair.on_for_rotations(70, 40, 0.7)
    while center_sensor.reflected_light_intensity > 30:
        steer_pair.on(70, 20)
    steer_pair.off()
    steer_pair.on_for_rotations(-70, 30, 0.05)
    timed_follower(center_sensor, 1, speed=30, kp=0.4)
    steer_pair.off()


Thread(target=look_at_blocks).start()
pick_up_block()
go_to_put_down()
