from sensor_and_motor_startup import *
from line_follower_class import *


def goto_blocks():
    while not steer_pair.wait_until_not_moving(motors=steer_pair):
        high_speed_follower()
    #stock_pid_follower(sensor=center_sensor, speed=60, side=-1)
    steer_pair.off()


goto_blocks()
