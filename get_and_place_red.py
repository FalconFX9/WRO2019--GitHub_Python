from line_follower_class import *

blocks = []
block_is_black = False
measuring = False


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
                blocks.append('white')
                sleep(0.3)
            elif 140 > average > 20:
                block_is_black = True
                measuring = False
                blocks.append('black')

    print('Thread look_at_blocks is finished')


def get_block():
    global block_is_black, duration
    turn_right(center_sensor)
    follow_for_xlines(3, center_sensor, line_sensor=left_side_sensor)
    steer_pair.off()
    turn_left(right_side_sensor)
    start_time = time()
    while not block_is_black:
        if not measuring:
            hisp_right_follower(speed=40, kp=0.1)
        else:
            steer_pair.off()
    steer_pair.off()
    duration = time() - start_time
    steer_pair.on_for_rotations(25, -30, 0.1)
    follow_to_line(right_side_sensor, center_sensor, 30, kp=0.2)
    steer_pair.off()
    value = []
    average = 0
    if duration < 1.2:
        for i in range(10):
            value.append(side_color_sensor.value(3))
            sleep(0.02)
        for intensity in value:
            average += intensity
        average = average / len(value)
        print(average)
        if average > 140:
            blocks.append('white')
        elif 140 > average > 20:
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


def placing(block_pos):
    global duration

    def place(pos):
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

    if duration < 1.2:
        # perform a 180 turn
        pass
        place(block_pos)
    else:
        turn_right(center_sensor)
        follow_to_line(line_sensor=right_side_sensor)
        steer_pair.off()
        turn_right(center_sensor)
        while not (right_side_sensor.value() == 5 or left_side_sensor.value() == 5):
            losp_center_follower(speed=30, kp=0.25)
        steer_pair.off()
        place(block_pos)
    lower_motor.on_for_degrees(10, 15)
    grabber_servo.on_for_degrees(20, 180)
    lower_motor.on_for_degrees(10, -50)


def run():
    get_block()
    placing(input('Pos'))