#!/usr/bin/env python3
from regrouped_functions import wro2019
from sensor_and_motor_startup import *

while not Button.buttons_pressed:
    pass
wro2019()
steer_pair.off(brake=False)
lower_motor.off(brake=False)
grabber_servo.off(brake=False)
