from line_follower_class import *
from threading import *

lower_motor.off()


def get_second_cable():

    def get_cable():
        global lines_passed
        left_side_sensor.mode = 'COL-REFLECT'
        right_side_sensor.mode = 'COL-REFLECT'
        while right_side_sensor.reflected_light_intensity > 30:
            steer_pair.on(-100, -30)
        steer_pair.on_for_rotations(100, -20, 0.07)
        steer_pair.off()
        t = Thread(target=check_for_lines, args=(2, ))
        t.start()
        while not lines_passed:
            losp_right_follower(speed=30)
        lines_passed = False
        steer_pair.off()
        steer_pair.on_for_rotations(-70, -60, 0.9)
        t = Thread(target=check_for_lines, args=(1, ))
        t.start()
        while not lines_passed:
            losp_left_follower(side_of_line=1, speed=30)
            print(left_side_sensor.reflected_light_intensity)
        steer_pair.off()
        lines_passed = False

    def pick_up_cable():
        lower_motor.on_for_degrees(speed=10, degrees=98)
        timed_follower(center_sensor, speed=20, timemax=0.83)
        steer_pair.off()
        lower_motor.on_for_degrees(speed=10, degrees=-100)

    get_cable()
    pick_up_cable()
