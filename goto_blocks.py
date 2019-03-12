from line_follower_class import *


def goto_blocks():
    global timemax
    timemax = time() + 5
    while time() < timemax:
        high_speed_follower()
    steer_pair.off()


goto_blocks()
