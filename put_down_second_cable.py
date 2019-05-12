from line_follower_class import *
from threading import *

lower_motor.off()
lines_passed = False


def put_down_second_cable():

    def check_for_lines(num_lines):
        global lines_passed
        counter = 0
        while counter < num_lines:
            print(counter)
            if center_sensor.reflected_light_intensity < 30:
                if counter < num_lines - 1:
                    counter = counter + 1
                    sleep(0.3)
                else:
                    counter = counter + 1
        lines_passed = True

    def goto_drop():
        global lines_passed, log_to_files
        steer_pair.on_for_rotations(70, 40, 1.56)
        while right_side_sensor.reflected_light_intensity > 30:
            steer_pair.on(70, 20)
        steer_pair.off()
        steer_pair.on_for_rotations(70, 40, 0.07)
        timed_follower(sensor=right_side_sensor, side_of_line=1, speed=30, kp=1, timemax=2.5)
        follow_to_line(following_sensor=right_side_sensor, line_sensor=center_sensor, side_of_line=1, speed=40,
                       kp=0.3)
        steer_pair.on_for_rotations(0, -40, 0.1)
        follow_for_xlines(3, sensor=right_side_sensor, side_of_line=1, ttarget=50, kp=0.25)
        steer_pair.off()
        lines_passed = False
        steer_pair.on_for_rotations(0, -20, 0.1)
        while center_sensor.reflected_light_intensity > 30:
            steer_pair.on(75, -30)
            print(center_sensor.reflected_light_intensity)
        steer_pair.off()
        steer_pair.on_for_rotations(100, -20, 0.17)
        follow_for_xlines(2, sensor=right_side_sensor, ttarget=45, kp=0.1, speed=40)
        steer_pair.off()
        lines_passed = False
        steer_pair.on_for_rotations(0, -30, 0.35)
        while center_sensor.reflected_light_intensity > 30:
            steer_pair.on(75, -30)
        steer_pair.off()
        left_side_sensor.mode = 'COL-COLOR'
        right_side_sensor.mode = 'COL-COLOR'
        wait = time() + 0.5
        while not (left_side_sensor.value() == 4 and right_side_sensor.value() == 3 and time() > wait):
            print('Left side : ' + str(left_side_sensor.value()) + 'Right side : ' + str(right_side_sensor.value()))
            losp_center_follower()
        steer_pair.off(brake=False)
        # Put down cable
        steer_pair.on_for_rotations(0, -30, 0.4)
        lower_motor.on_for_degrees(speed=30, degrees=85)
        sleep(0.8)
        steer_pair.on_for_rotations(0, 60, 1.15)
        lower_motor.on_for_degrees(speed=30, degrees=-85)
        log_to_files = False
        left_side_sensor.mode = 'COL-REFLECT'
        right_side_sensor.mode = 'COL-REFLECT'

    goto_drop()
