from line_follower_class import *
from threading import *

side_color_sensor.mode = 'RGB'
block_is_black = False
block_left = False
blocks_passed = 0


class BlackOrWhite:

    def __init__(self):
        self.light_intensity = side_color_sensor.value(3)
        self.t2 = Thread(target=self.look_at_blocks, args=())

    def look_at_blocks(self):
        global block_is_black, block_left, blocks_passed
        while not block_is_black:
            if side_color_sensor.value(3) > 100:
                sleep(0.3)
            elif 100 > side_color_sensor.value(3) > 40:
                block_is_black = True
        print('Thread look_at_blocks is finished')

    def start_t2(self):
        self.t2.start()


def turn_and_pick_up():
    global block_left, block_is_black, blocks_passed, t_time
    start_time = time()
    while not block_is_black:
        hisp_right_follower(speed=40, kp=0.15)
    steer_pair.off()
    t_time = time() - start_time
    print(t_time)
    block_is_black = False
    steer_pair.on_for_rotations(0, -30, 0.1)
    follow_to_line(following_sensor=right_side_sensor, line_sensor=center_sensor, speed=30, kp=0.1)
    if blocks_passed > 2:
        steer_pair.on_for_rotations(0, 30, 0.3)
    steer_pair.off()
    lower_motor.on_for_degrees(10, -10)
    steer_pair.on_for_rotations(0, 30, 0.15)
    steer_pair.on_for_rotations(60, 40, 1.14)
    steer_pair.on_for_rotations(0, 20, 0.2)
    lower_motor.on_for_degrees(10, 50)
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
lower_motor.on_for_degrees(10, -3)
t = BlackOrWhite()
t.start_t2()
turn_and_pick_up()
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
steer_pair.on_for_rotations(0, -40, 0.7)
steer_pair.on_for_rotations(-70, 40, 0.7)
while right_side_sensor.reflected_light_intensity > 30:
    steer_pair.on(-70, 30)
steer_pair.off()
steer_pair.on_for_rotations(-70, -40, 0.05)
follow_to_line(following_sensor=center_sensor, line_sensor=right_side_sensor, speed=40, kp=0.3)
steer_pair.off()
steer_pair.on_for_rotations(0, -40, 0.7)
steer_pair.on_for_rotations(70, 40, 0.7)
while right_side_sensor.reflected_light_intensity > 30:
    steer_pair.on(70, 20)
steer_pair.off()
steer_pair.on_for_rotations(-70, -30, 0.05)
timed_follower(center_sensor, 1.5, speed=30, kp=0.3)
steer_pair.off()
'''
while not 100 > side_color_sensor.value(3) > 40:
    hisp_right_follower(speed=30, kp=0.1)
steer_pair.off(brake=False)
timed_follower(right_side_sensor, timemax=0.75, speed=40, ttarget=45)
steer_pair.off()
lower_motor.on_for_degrees(10, -10)
steer_pair.on_for_rotations(0, 30, 0.15)
steer_pair.off()
grabber_servo.on_for_degrees(10, -180)
steer_pair.on_for_rotations(60, 40, 1.14)
steer_pair.off()
steer_pair.on_for_rotations(0, 20, 0.2)
steer_pair.off()
lower_motor.on_for_degrees(10, 53)
timed_follower(sensor=center_sensor, timemax=0.65, speed=20, kp=0.35, side_of_line=1)
steer_pair.off()
lower_motor.on_for_degrees(10, -52)
lower_motor.off()
'''
