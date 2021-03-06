from line_follower_class import *
from threading import Thread
# from start_sequence import position

side_color_sensor.mode = 'RGB'
block_is_black = False
t_time = 0
measuring = False
blocks = []


def look_at_blocks():
    global block_is_black, measuring
    value = []
    average = 0
    while not block_is_black:
        if center_sensor.reflected_light_intensity < 30:
            steer_pair.off()
            measuring = True

            # Sensor runs at 50Hz, so this represents 0.5s --sleep just in case
            for i in range(10):
                value.append(side_color_sensor.value(3))
                sleep(0.02)
            for intensity in value:
                average += intensity
            average = average / len(value)
            print(average)
            if average > 140:
                measuring = False
                blocks.append('white')
                sleep(0.3)
            elif 140 > average > 20:
                block_is_black = True
                measuring = False
                blocks.append('black')

    print('Thread look_at_blocks is finished')


def pick_up_block():
    global block_is_black, t_time
    right_side_sensor.mode = 'COL-REFLECT'
    lower_motor.off(brake=False)
    lower_motor.off()
    start_time = time()
    while not block_is_black:
        if not measuring:
            hisp_right_follower(speed=40, kp=0.1)
        else:
            steer_pair.off()
    steer_pair.off()
    t_time = time() - start_time
    print(t_time)
    steer_pair.on_for_rotations(25, -30, 0.1)
    follow_to_line(right_side_sensor, center_sensor, 30, kp=0.2)
    steer_pair.off()
    value = []
    average = 0
    if t_time < 1.2:
        for i in range(10):
            value.append(side_color_sensor.value(3))
            sleep(0.02)
        for intensity in value:
            average += intensity
        average = average / len(value)
        print(average)
        if average > 140:
            blocks.append('white')
            sleep(0.3)
        elif 140 > average > 40:
            blocks.append('black')
        if 'white' in blocks:
            blocks.append('black')
        else:
            blocks.append('white')
    else:
        blocks.append('black')
    lower_motor.on_for_degrees(10, -10)
    steer_pair.on_for_rotations(60, 40, 1.2)
    while center_sensor.reflected_light_intensity > 30:
        steer_pair.on(60, 15)
    steer_pair.off()
    steer_pair.on_for_rotations(0, 20, 0.2)
    lower_motor.on_for_degrees(20, 58)
    sleep(0.6)
    timed_follower(sensor=center_sensor, timemax=0.45, speed=40, kp=0.25, ttarget=30)
    steer_pair.off()
    lower_motor.on_for_degrees(10, -52)


def go_to_put_down():
    global t_time
    # add turn towards wall and lower turn to position
    steer_pair.on_for_rotations(0, -40, 0.25)
    steer_pair.on_for_rotations(-70, 40, 0.7)
    while right_side_sensor.reflected_light_intensity > 30:
        steer_pair.on(-70, 30)
    steer_pair.off()
    if t_time < 1.2:
        follow_for_xlines(3, sensor=right_side_sensor, speed=50, ttarget=45, kp=0.2)
        steer_pair.off()
    else:
        follow_for_xlines(2, sensor=right_side_sensor, speed=50, ttarget=45, kp=0.2)
        steer_pair.off()
    steer_pair.on_for_rotations(0, -40, 0.35)
    steer_pair.on_for_rotations(-70, 40, 0.55)
    while right_side_sensor.reflected_light_intensity > 30:
        steer_pair.on(-70, 30)
    steer_pair.off()
    steer_pair.on_for_rotations(-70, 40, 0.1)
    follow_to_line(following_sensor=right_side_sensor, line_sensor=center_sensor, speed=40, kp=0.65)
    steer_pair.off()
    steer_pair.on_for_rotations(0, -40, 0.65)
    steer_pair.on_for_rotations(-70, 40, 0.7)
    while left_side_sensor.reflected_light_intensity > 30:
        steer_pair.on(-70, 30)
    steer_pair.off()
    steer_pair.on_for_rotations(70, 40, 0.05)
    follow_to_line(following_sensor=left_side_sensor, line_sensor=right_side_sensor, side_of_line=1, speed=30, kp=0.4)
    steer_pair.off()
    steer_pair.on_for_rotations(0, -40, 0.65)
    steer_pair.on_for_rotations(70, 40, 0.7)
    while center_sensor.reflected_light_intensity > 30:
        steer_pair.on(70, 20)
    steer_pair.off()
    steer_pair.on_for_rotations(-70, 30, 0.05)


def put_down_blocks(block_pos: int):
    right_side_sensor.mode = 'COL-COLOR'
    left_side_sensor.mode = 'COL-COLOR'
    while not (right_side_sensor.value() == 2 or left_side_sensor.value() == 2):
        losp_center_follower(speed=30, kp=0.25)
    # timed_follower(center_sensor, 0.7, speed=30, kp=0.4)
    steer_pair.off()
    grabber_servo.on_for_degrees(30, block_pos)
    sleep(1.5)
    steer_pair.on_for_rotations(0, 30, 0.2)
    if block_pos == 360:
        steer_pair.on_for_rotations(0, 20, 0.06)
    lower_motor.on_for_degrees(10, 45)
    sleep(0.5)
    if block_pos == 360:
        oscillate(0.07)
    else:
        oscillate(0.07)
    lower_motor.on_for_degrees(10, 15)
    grabber_servo.on_for_degrees(20, 180)
    lower_motor.on_for_degrees(10, -50)


def get_blocks_from_side():
    follow_for_xlines(2, left_side_sensor, speed=40, kp=0.2, ttarget=40)
    steer_pair.off()
    steer_pair.on_for_rotations(0, -40, 0.67)
    steer_pair.on_for_rotations(72, 40, 0.9)
    while center_sensor.reflected_light_intensity > 30:
        steer_pair.on(70, 20)
    steer_pair.off()
    steer_pair.on_for_rotations(0, 40, 0.6)


def oscillate(speed):
    steer_pair.on_for_seconds(100, 50, speed)
    steer_pair.on_for_seconds(-100, 50, speed)
    steer_pair.on_for_seconds(100, 50, speed)
    steer_pair.on_for_seconds(-100, 50, speed)
    steer_pair.on_for_seconds(100, 50, speed)
    steer_pair.on_for_seconds(-100, 50, speed)
    steer_pair.on_for_seconds(100, 50, speed)
    steer_pair.on_for_seconds(-100, 50, speed)


def pick_up_blue_block():
    side_color_sensor.mode = 'RGB'
    right_side_sensor.mode = 'COL-REFLECT'
    # get_blocks_from_side()
    lower_motor.off()
    Thread(target=look_at_blocks).start()
    pick_up_block()
    go_to_put_down()
    block_num = (int(input('Enter bloc position')) * 90) + 180
    put_down_blocks(block_num)
    print(blocks)
    lower_motor.off(brake=False)
    grabber_servo.off(brake=False)


pick_up_blue_block()
