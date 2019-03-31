from line_follower_class import *

lower_motor.off(brake=True)
lower_motor.on_for_degrees(10, -10)
steer_pair.on_for_rotations(60, 40, 1.06)
steer_pair.on_for_rotations(0, 20, 0.3)
lower_motor.on_for_degrees(10, 65)
grabber_servo.on_for_degrees(10, -90)
timed_follower(sensor=center_sensor, timemax=0.5, speed=20)
lower_motor.on_for_degrees(10, -75)
