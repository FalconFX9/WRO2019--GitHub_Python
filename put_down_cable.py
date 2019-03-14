from line_follower_class import *
from threading import *

counter = 0
check = True
reset = False
numlines = 0


def put_down_cable():

    def check_for_lines():
        global counter, numlines, reset, check
        while check:
            if reset:
                counter = 0
                reset = False
            else:
                if center_sensor.reflected_light_intensity < 30:
                    if counter < numlines - 1:
                        counter = counter + 1
                    else:
                        counter = counter + 1
                        sleep(0.5)
            print(counter)

    def goto_drop():
        global numlines, reset, counter, check
        steer_pair.on_for_rotations(100, -30, 3)
        sleep(4)
        numlines = 1
        while not counter == 1:
            hisp_left_follower(side_of_line=1, speed=40)
        steer_pair.off()
        steer_pair.on_for_rotations(-70, -30, 1)
        sleep(4)
        numlines = 2
        while not counter == 2:
            hisp_right_follower(speed=40)
        steer_pair.off()
        check = False
        steer_pair.on_for_rotations(70, -30, 1)
        sleep(4)
        left_side_sensor.mode = 'COLOR'
        while not left_side_sensor.value() == 8:
            losp_center_follower(side_of_line=1)
        steer_pair.off()
        left_side_sensor.mode = 'RGB'
        lower_motor.on_for_degrees(speed=10, degrees=90)

    t = Thread(target=check_for_lines)
    t.start()
    goto_drop()


put_down_cable()
