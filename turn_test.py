from line_follower_class import *
from threading import *

side_color_sensor.mode = 'RGB'
block_is_black = False
block_left = False
blocks_passed = 0
stop_log = False


class BlackOrWhite:

    def __init__(self):
        self.light_intensity = side_color_sensor.value(3)
        self.t = Thread(target=self.count_blocks_passed, args=())
        self.t2_5 = Thread(target=self.count_blocks_passed, args=())
        self.t2 = Thread(target=self.look_at_blocks, args=())

    def count_blocks_passed(self):
        global blocks_passed
        blocks_passed = 0
        while not (blocks_passed == 3 and stop_log):
            if self.light_intensity > 40:
                blocks_passed += 1
                sleep(0.3)
        print('Thread count_blocks_passed is finished')

    def look_at_blocks(self):
        global block_is_black, block_left, blocks_passed
        while not block_is_black:
            if side_color_sensor.value(3) > 100:
                sleep(0.3)
            elif 100 > side_color_sensor.value(3) > 40:
                block_is_black = True
        print('Thread look_at_blocks is finished')

    def start_t(self):
        self.t.start()

    def start_t2(self):
        self.t2.start()

    def start_t2_5(self):
        self.t2_5.start()


def turn_and_pick_up():
    global block_left, block_is_black, stop_log, blocks_passed
    while not block_is_black:
        hisp_right_follower(speed=40, side_of_line=1)
    steer_pair.off()
    block_is_black = False
    steer_pair.on_for_rotations(0, -30, 0.1)
    follow_to_line(following_sensor=right_side_sensor, line_sensor=center_sensor, speed=30, kp=0.1)
    stop_log = True
    if blocks_passed > 2:
        steer_pair.on_for_rotations(0, 30, 0.3)
    steer_pair.off()
    lower_motor.on_for_degrees(10, -10)
    steer_pair.on_for_rotations(0, 30, 0.15)
    steer_pair.on_for_rotations(60, 40, 1.14)
    steer_pair.on_for_rotations(0, 20, 0.2)
    lower_motor.on_for_degrees(10, 58)
    if not block_left:
        grabber_servo.on_for_degrees(10, -90)
        block_left = True
    else:
        grabber_servo.on_for_degrees(10, -180)
        block_left = False
    timed_follower(sensor=center_sensor, timemax=0.65, speed=20, kp=0.35, side_of_line=1)
    steer_pair.off()
    lower_motor.on_for_degrees(10, -52)


lower_motor.off()
t = BlackOrWhite()
t.start_t()
t.start_t2()
turn_and_pick_up()
lower_motor.off()
# sleep(5)
# t.start_t2_5()
# turn_and_pick_up()
