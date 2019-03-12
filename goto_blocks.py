from sensor_and_motor_startup import *
from line_follower_class import *


def goto_blocks():
    high_speed_follower()
    #stock_pid_follower(sensor=center_sensor, speed=60, side=-1)
    steer_pair.off()


goto_blocks()
