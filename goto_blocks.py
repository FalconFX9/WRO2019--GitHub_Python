from sensor_and_motor_startup import *


def goto_blocks():
    timemax = time() + 3
    while time() < timemax:
        stock_pid_follower(sensor=center_sensor, speed=60, side=-1)
    steer_pair.off()


goto_blocks()
