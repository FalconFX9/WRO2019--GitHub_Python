from sensor_and_motor_startup import *


def goto_blocks():
    while not time() < time() + 5:
        stock_pid_follower(sensor=line_1, speed=60, side=0)
    steer_pair.off()
