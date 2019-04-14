from line_follower_class import *
import threading

lines_passed = False


def goto_cables_group():
    lower_motor.off(brake=True)

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

    def goto_cable():
        global lines_passed, log_to_files
        print('Going to the first cable')
        timed_follower(sensor=right_side_sensor, timemax=3.6, side_of_line=1, speed=85, kp=0.3, ttarget=50)
        t = threading.Thread(target=check_for_lines, args=(1,))
        t.start()
        while not lines_passed:
            hisp_right_follower(side_of_line=1, speed=45)
        steer_pair.off()
        log_to_files = False
        lines_passed = False

    def pick_up_cable():
        lower_motor.on_for_degrees(speed=30, degrees=90)
        timed_follower(center_sensor, side_of_line=1, speed=30, timemax=1.1, kp=0.2)
        steer_pair.off()
        lower_motor.on_for_degrees(speed=10, degrees=-90)

    def turn_around():
        steer_pair.on_for_rotations(-70, 40, 1.7)
        while center_sensor.reflected_light_intensity > 30:
            steer_pair.on(-70, 40)
        steer_pair.off()
        steer_pair.on_for_rotations(70, 60, 0.05)
        steer_pair.off()

    goto_cable()
    pick_up_cable()
    turn_around()
