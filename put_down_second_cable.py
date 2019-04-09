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
        follow_to_line(following_sensor=right_side_sensor, line_sensor=left_side_sensor, speed=40, side_of_line=1,
                       kp=0.5)
        t = Thread(target=check_for_lines, args=(5, ))
        t.start()
        while not lines_passed:
            hisp_right_follower(speed=60, side_of_line=1, kp=0.15)
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
        steer_pair.on_for_rotations(-75, -30, 0.05)
        steer_pair.off()
        left_side_sensor.mode = 'COL-COLOR'
        right_side_sensor.mode = 'COL-COLOR'
        wait = time() + 0.5
        while not (left_side_sensor.value() == 4 and right_side_sensor.value() == 3 and time() > wait):
            print('Left side : ' + str(left_side_sensor.value()) + 'Right side : ' + str(right_side_sensor.value()))
            losp_center_follower(side_of_line=1)
        steer_pair.off(brake=False)
        log_to_files = False
        left_side_sensor.mode = 'COL-REFLECT'
        right_side_sensor.mode = 'COL-REFLECT'

    def put_down_cable():
        steer_pair.on_for_rotations(0, -30, 0.1)
        lower_motor.on_for_degrees(speed=10, degrees=90)
        steer_pair.on_for_rotations(0, 30, 0.5)
        lower_motor.on_for_degrees(speed=10, degrees=-90)

    goto_drop()
    put_down_cable()
