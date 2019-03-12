from line_follower_class import *


def goto_blocks():
    global timemax
    timemax = time() + 5
    while time() < timemax:
        losp_right_follower()
    steer_pair.off()


goto_blocks()
