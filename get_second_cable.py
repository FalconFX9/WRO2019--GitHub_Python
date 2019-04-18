from line_follower_class import *
from threading import *

lower_motor.off()
lines_passed = False


def get_second_cable():

    def check_for_lines(num_lines, sensor=center_sensor):
        global lines_passed
        counter = 0
        while counter < num_lines:
            print(counter)
            if sensor.reflected_light_intensity < 30:
                if counter < num_lines - 1:
                    counter = counter + 1
                    sleep(0.3)
                else:
                    counter = counter + 1
        lines_passed = True

    def get_cable():
        global lines_passed
        left_side_sensor.mode = 'COL-REFLECT'
        right_side_sensor.mode = 'COL-REFLECT'
        while right_side_sensor.reflected_light_intensity > 30:
            steer_pair.on(-100, -30)
        steer_pair.on_for_rotations(100, -20, 0.07)
        steer_pair.off()
        follow_for_xlines(2, sensor=right_side_sensor, side_of_line=1, ttarget=45, kp=0.25)
        lines_passed = False
        steer_pair.off()
        steer_pair.on_for_rotations(-70, -75, 0.9)
        while left_side_sensor.reflected_light_intensity > 30:
            steer_pair.on(-70, -20)
        steer_pair.off()
        follow_to_line(left_side_sensor, right_side_sensor, speed=40, side_of_line=1, kp=0.3)
        steer_pair.off()
        lines_passed = False

    def pick_up_cable():
        lower_motor.on_for_degrees(speed=10, degrees=90)
        timed_follower(center_sensor, speed=30, timemax=0.94)
        steer_pair.off()
        lower_motor.on_for_degrees(speed=10, degrees=-100)
        steer_pair.on_for_rotations(0, 30, 0.4)

    get_cable()
    pick_up_cable()
