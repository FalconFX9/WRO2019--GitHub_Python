from sensor_and_motor_startup import *


def goto_blocks():
    timemax = time() + 5
    while time() < timemax:
        stock_pid_follower(sensor=line_1, speed=30, side=0)
    steer_pair.off()