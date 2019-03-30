from line_follower_class import *
import threading

lines_passed = False
count = 0
file_s = open('sensor_data.txt', 'w+')
file_x = open('time_data.txt', 'w+')
loging = True


def goto_cables_group():
    lower_motor.off(brake=True)

    def check_for_lines(num_lines):
        global lines_passed, count
        count = 0
        while count < num_lines:
            if left_side_sensor.reflected_light_intensity < 30:
                if count < num_lines - 1:
                    beep = Sound()
                    count = count + 1
                    beep.beep()
                    sleep(0.5)
                else:
                    count = count + 1
        lines_passed = True

    def log_data():
        global file_x, file_s, loging
        starttime = time()
        while loging:
            file_s.write(str(center_sensor.reflected_light_intensity) + '\n')
            file_x.write(str(round((time() - starttime), 1)) + '\n')
            sleep(0.1)
        file_x.close()
        file_s.close()

    def goto_cable():
        global loging
        t2 = threading.Thread(target=log_data)
        t2.start()
        timed_follower(sensor=right_side_sensor, timemax=3.6, side_of_line=1, speed=60, kp=0.2, ttarget=50)
        loging = False
        t = threading.Thread(target=check_for_lines, args=(1,))
        t.start()
        while not lines_passed:
            hisp_right_follower(side_of_line=1, speed=30)
        steer_pair.off()

    def pick_up_cable():
        lower_motor.on_for_degrees(speed=10, degrees=90)
        timed_follower(center_sensor, side_of_line=1, speed=20, timemax=0.85, kp=0.3)
        steer_pair.off()
        lower_motor.on_for_degrees(speed=10, degrees=-90)

    def turn_around():
        global lines_passed
        steer_pair.on_for_rotations(-70, 40, 1.5)
        sleep(3)

    goto_cable()
    pick_up_cable()
    turn_around()
