from line_follower_class import *
import threading

lines_passed = False


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


def goto_blocks():
    steer_pair.on_for_rotations(20, -20, 0.6)
    while not lines_passed:
        hisp_right_follower(speed=30)
    steer_pair.off()


t = threading.Thread(target=check_for_lines, args=(4, ))
t.start()
goto_blocks()
