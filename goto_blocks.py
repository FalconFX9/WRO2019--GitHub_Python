from line_follower_class import *
import threading

lines_passed = False
lower_motor.off(brake=True)


def check_for_lines(num_lines):
    global lines_passed
    count = 0
    while count < num_lines:
        if center_sensor.reflected_light_intensity < 30:
            if count < num_lines - 1:
                beep = Sound()
                count = count + 1
                beep.beep()
                sleep(0.5)
            else:
                count = count + 1
    lines_passed = True


def goto_cable():
    steer_pair.on_for_rotations(20, -20, 0.6)
    while not lines_passed:
        hisp_right_follower(speed=40)
    steer_pair.off()


def pick_up_cable():
    lower_motor.on_for_degrees(speed=10, degrees=80)
    timed_follower(center_sensor, side_of_line=1, speed=20, timemax=0.8)
    steer_pair.off()
    lower_motor.on_for_degrees(speed=10, degrees=-70)


t = threading.Thread(target=check_for_lines, args=(5, ))
t.start()
goto_cable()
pick_up_cable()
