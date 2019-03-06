from sensor_and_motor_startup import *


def goto_blocks():
    while not time.time() < time.time() + 5:
        stock_pid_follower(sensor=line_1, speed=60)
    steer_pair.off()
