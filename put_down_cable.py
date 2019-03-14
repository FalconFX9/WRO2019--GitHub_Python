from line_follower_class import *
from threading import *

counter = 0
lines_passed = False


def put_down_cable():

    def check_for_lines(num_lines):
        global lines_passed, counter
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
        t = Thread(target=check_for_lines, args=(1,))
        t.start()
        while not lines_passed:
            hisp_left_follower(side_of_line=1, speed=40)
        steer_pair.off()
        steer_pair.on_for_rotations(0, -40, 0.3)
        steer_pair.on_for_rotations(-70, -30, 1.2)
        lines_passed = False
        t = Thread(target=check_for_lines, args=(2,))
        t.start()
        while not lines_passed:
            hisp_right_follower(speed=30)
        steer_pair.off()
        steer_pair.on_for_rotations(0, -30, 0.14)
        steer_pair.on_for_rotations(75, -30, 1.1)
        left_side_sensor.mode = 'COLOR'
        right_side_sensor.mode = 'COLOR'
        print(left_side_sensor.value())
        print(right_side_sensor.value())
        while not left_side_sensor.value() == 8 and right_side_sensor.value() == 3:
            print(left_side_sensor.value())
            print(right_side_sensor.value())
            losp_center_follower(side_of_line=1)
        steer_pair.off()
        left_side_sensor.mode = 'RGB'
        right_side_sensor.mode = 'RGB'
        lower_motor.on_for_degrees(speed=10, degrees=90)
        steer_pair.on_for_rotations(0, 30, 0.5)
        lower_motor.on_for_degrees(speed=10, degrees=-90)

    lower_motor.off()
    goto_drop()


put_down_cable()
