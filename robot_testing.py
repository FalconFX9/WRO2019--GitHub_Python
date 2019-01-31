from ev3dev2.auto import *
import time
from time import sleep
from PID_Line_Follower import sensor_declaration, pid_line_follower


timelimit = time.time() + 5
sensor_declaration()

steer_pair = 'null'
try:
    steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
except DeviceNotFound:
    print('Main motors not found')

grabber_servo = 'null'
try:
    grabber_servo = MediumMotor(OUTPUT_A)
except DeviceNotFound:
    print('Main servo not found')

steer_pair.on_for_seconds(-40, 3)
grabber_servo.on_for_rotations(-100, 10)
if grabber_servo.is_stalled:
    grabber_servo.off(brake=True)
    sleep(5)
grabber_servo.on_for_rotations(100, 11)
if grabber_servo.is_stalled:
    grabber_servo.off(brake=True)