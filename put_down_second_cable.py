from line_follower_class import *
from threading import *

lines_passed = False
lower_motor.off()


def put_down_second_cable():

    def check_for_lines(num_lines):
        global lines_passed
        counter = 0
        while counter < num_lines:
            if center_sensor.reflected_light_intensity < 30:
                if counter < num_lines - 1:
                    beep = Sound()
                    counter = counter + 1
                    beep.beep()
                    sleep(0.3)
                else:
                    counter = counter + 1
        lines_passed = True

    def goto_drop():
        global lines_passed
        follow_to_line(following_sensor=right_side_sensor, line_sensor=left_side_sensor, speed=30, side_of_line=1)
        t = Thread(target=check_for_lines, args=(4, ))
        t.start()
        while not lines_passed:
            hisp_right_follower(speed=40, side_of_line=1)
        steer_pair.off()
        lines_passed = False
        steer_pair.on_for_rotations(0, -20, 0.1)
        while center_sensor.reflected_light_intensity > 30:
            steer_pair.on(75, -30)
            print(center_sensor.reflected_light_intensity)
        steer_pair.off()
        steer_pair.on_for_rotations(100, -20, 0.2)
        t = Thread(target=check_for_lines, args=(1,))
        t.start()
        while not lines_passed:
            losp_right_follower()
        steer_pair.off()
        steer_pair.on_for_rotations(0, -30, 0.18)
        while center_sensor.reflected_light_intensity > 30:
            steer_pair.on(75, -30)
        steer_pair.off()
        left_side_sensor.mode = 'COLOR'
        right_side_sensor.mode = 'COLOR'
        wait = time() + 0.5
        while not (left_side_sensor.value() == 5 and right_side_sensor.value() == 4 and time() > wait):
            losp_center_follower(side_of_line=1)
        steer_pair.off()
        left_side_sensor.mode = 'RGB'
        right_side_sensor.mode = 'RGB'

    def put_down_cable():
        lower_motor.on_for_degrees(speed=10, degrees=90)
        steer_pair.on_for_rotations(0, 30, 0.5)
        lower_motor.on_for_degrees(speed=10, degrees=-90)

    goto_drop()
    put_down_cable()


put_down_second_cable()
