from line_follower_class import *


def goto_blocks():
    steer_pair.on_for_rotations(20, -20, 0.6)
    count = 0
    while count < 4:
        hisp_center_follower(side_of_line=1)
        if left_side_sensor.value(3) > 100:
            count = count + 1
            sleep(0.3)
    steer_pair.off()


goto_blocks()
