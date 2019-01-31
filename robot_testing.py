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

steer_pair.on_for_seconds(steering=0, speed=-40, seconds=3)
grabber_servo.on_for_rotations(-100, 10)
if grabber_servo.is_stalled:
    grabber_servo.off(brake=True)
    sleep(5)
grabber_servo.on_for_rotations(100, 11)
if grabber_servo.is_stalled:
    grabber_servo.off(brake=True)
