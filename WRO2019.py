#!/usr/bin/env python3
from regrouped_functions import wro2019
from sensor_and_motor_startup import *

while True:
    if Button().enter:
        break
wro2019()
steer_pair.off(brake=False)
lower_motor.off(brake=False)
grabber_servo.off(brake=False)
