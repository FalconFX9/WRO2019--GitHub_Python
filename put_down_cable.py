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
                    sleep(0.5)
                else:
                    counter = counter + 1
            print(counter)
        lines_passed = True

    def goto_drop():
        global lines_passed
        steer_pair.on_for_rotations(100, -30, 2)
        sleep(4)
        t = Thread(target=check_for_lines, args=(1,))
        t.start()
        while not lines_passed:
            hisp_left_follower(side_of_line=1, speed=40)
        steer_pair.off()
        steer_pair.on_for_rotations(-70, -30, 1)
        sleep(4)
        lines_passed = False
        t = Thread(target=check_for_lines, args=(2,))
        t.start()
        while not lines_passed:
            hisp_right_follower(speed=40)
        steer_pair.off()
        steer_pair.on_for_rotations(70, -30, 1)
        sleep(4)
        left_side_sensor.mode = 'COLOR'
        while not left_side_sensor.value() == 8:
            losp_center_follower(side_of_line=1)
        steer_pair.off()
        left_side_sensor.mode = 'RGB'
        lower_motor.on_for_degrees(speed=10, degrees=90)

    goto_drop()


put_down_cable()
