#!/usr/bin/env python3
from ev3dev2.auto import *
import time
from time import sleep

timelimit = time.time() + 5
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
try:
    steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
except DeviceNotFound:
    print('Main motors not found')

grabber_servo = MediumMotor(OUTPUT_A)
try:
    grabber_servo = MediumMotor(OUTPUT_A)
except DeviceNotFound:
    print('Main servo not found')

grabber_servo.on_for_rotations(-100, 10)
if grabber_servo.is_stalled:
    grabber_servo.off(brake=True)
    sleep(1)

steer_pair.on_for_rotations(0, -20, 3)

grabber_servo.on_for_rotations(100, 10)
if grabber_servo.is_stalled:
    grabber_servo.off(brake=True)
    sleep(5)
