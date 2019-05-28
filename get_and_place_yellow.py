from line_follower_class import *
from threading import Thread


def oscillate(speed):
    steer_pair.on_for_seconds(100, 50, speed)
    steer_pair.on_for_seconds(-100, 50, speed)
    steer_pair.on_for_seconds(100, 50, speed)
    steer_pair.on_for_seconds(-100, 50, speed)
    steer_pair.on_for_seconds(100, 50, speed)
    steer_pair.on_for_seconds(-100, 50, speed)
    steer_pair.on_for_seconds(100, 50, speed)
    steer_pair.on_for_seconds(-100, 50, speed)


def measure():
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
                sleep(0.3)
            elif 140 > average > 20:
                block_is_black = True
                measuring = False

    print('Thread look_at_blocks is finished')


def pick_up_last_block():
    global block_is_black, measuring
    steer_pair.on_for_rotations(0, 40, 0.3)
    turn_right(right_side_sensor)
    steer_pair.on_for_rotations(-100, 40, 0.05)
    start_time = time()
    Thread(target=measure).start()
    while not block_is_black:
        if not measuring:
            hisp_right_follower(speed=40, kp=0.15)
        else:
            steer_pair.off()
    duration = time() - start_time
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
    turn_left(right_side_sensor)
    if duration < 1.2:
        follow_for_xlines(2, right_side_sensor)
    else:
        follow_to_line(right_side_sensor)
    steer_pair.off()
    steer_pair.on_for_rotations(0, -40, 0.15)
    turn_left(right_side_sensor)
    steer_pair.on_for_rotations(100, 40, 0.05)
    follow_for_xlines(3, right_side_sensor, 1)
    steer_pair.off()

    steer_pair.on_for_rotations(0, -40, 0.67)
    steer_pair.on_for_rotations(-72, 40, 0.9)
    while center_sensor.reflected_light_intensity > 30:
        steer_pair.on(-70, 20)
    steer_pair.off()
    steer_pair.on_for_rotations(0, 40, 0.6)


def put_down_last_block():
    left_side_sensor.mode, right_side_sensor.mode = 'COL-COLOR', 'COL-COLOR'
    while not (right_side_sensor.value() == 5 or left_side_sensor.value() == 5):
        losp_center_follower(speed=30, kp=0.25)
    steer_pair.off()
    pos = int(input('pos '))
    grabber_servo.on_for_degrees(30, (pos * 90) + 180)
    sleep(1.5)
    steer_pair.on_for_rotations(0, 30, 0.2)
    if pos == 360:
        steer_pair.on_for_rotations(0, 20, 0.06)
    lower_motor.on_for_degrees(10, 45)
    sleep(0.5)
    if pos == 360:
        oscillate(0.07)
    else:
        oscillate(0.07)


def run():
    pick_up_last_block()
    put_down_last_block()


run()
