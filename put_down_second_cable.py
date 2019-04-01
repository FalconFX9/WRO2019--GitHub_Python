from line_follower_class import *
from threading import *

lower_motor.off()


def put_down_second_cable():

    def goto_drop():
        global lines_passed, log_to_files
        steer_pair.on_for_rotations(70, 40, 1.56)
        while right_side_sensor.reflected_light_intensity > 30:
            steer_pair.on(70, 20)
        steer_pair.off()
        steer_pair.on_for_rotations(70, 40, 0.07)
        follow_to_line(following_sensor=right_side_sensor, line_sensor=left_side_sensor, speed=30, side_of_line=1,
                       kp=0.38)
        t = Thread(target=check_for_lines, args=(5, ))
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
        steer_pair.on_for_rotations(100, -20, 0.17)
        t = Thread(target=check_for_lines, args=(2,))
        t.start()
        while not lines_passed:
            losp_right_follower()
        steer_pair.off()
        lines_passed = False
        steer_pair.on_for_rotations(0, -30, 0.35)
        while center_sensor.reflected_light_intensity > 30:
            steer_pair.on(75, -30)
        steer_pair.off()
        left_side_sensor.mode = 'COL-COLOR'
        right_side_sensor.mode = 'COL-COLOR'
        wait = time() + 0.5
        while not (left_side_sensor.value() == 4 and right_side_sensor.value() == 6 and time() > wait):
            losp_center_follower(side_of_line=1)
        steer_pair.off()
        log_to_files = False
        left_side_sensor.mode = 'COL-REFLECT'
        right_side_sensor.mode = 'COL-REFLECT'

    def put_down_cable():
        lower_motor.on_for_degrees(speed=10, degrees=90)
        steer_pair.on_for_rotations(0, 30, 0.5)
        lower_motor.on_for_degrees(speed=10, degrees=-90)

    goto_drop()
    put_down_cable()
