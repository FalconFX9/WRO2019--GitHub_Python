from line_follower_class import *
from threading import *

lines_passed = False


def put_down_cable():
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
        global lines_passed
        left_side_sensor.mode = 'COL-REFLECT'
        right_side_sensor.mode = 'COL-REFLECT'
        follow_to_line(line_sensor=right_side_sensor, speed=40, side_of_line=1)
        steer_pair.off()
        steer_pair.on_for_rotations(0, -40, 0.3)
        # steer_pair.on_for_rotations(-100, -20, 0.4)
        while right_side_sensor.reflected_light_intensity > 30:
            steer_pair.on(-100, -20)
        steer_pair.on_for_rotations(100, -20, 0.05)
        lines_passed = False
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
        steer_pair.on_for_rotations(-75, -30, 0.03)
        wait = time() + 0.5
        print("Switching modes")
        left_side_sensor.mode = 'COL-COLOR'
        right_side_sensor.mode = 'COL-COLOR'
        while not (left_side_sensor.value() == 5 and right_side_sensor.value() == 2 and time() > wait):
            losp_center_follower(side_of_line=1)
        steer_pair.off()
        lower_motor.on_for_degrees(speed=10, degrees=90)
        steer_pair.on_for_rotations(0, 60, 0.65)
        lower_motor.on_for_degrees(speed=10, degrees=-90)

    lower_motor.off()
    goto_drop()
