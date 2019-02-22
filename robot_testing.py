#!/usr/bin/env python3
from time import *
from sensor_and_motor_startup import *

sensor_declaration()
motor_initialization()

while time() < time() + 10:
    stock_pid_follower(sensor=line_1, side=1, speed=80)
