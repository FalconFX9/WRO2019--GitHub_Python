from sensor_and_motor_startup import *


def goto_blocks():
    stock_pid_follower(sensor=line_1)
    sleep(5)
    steer_pair.off()
