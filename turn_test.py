from line_follower_class import *

lower_motor.off(brake=True)

while not side_color_sensor.value() == 0:
    hisp_right_follower(speed=30)


def turn_and_pick_up():
    lower_motor.on_for_degrees(10, -10)
    steer_pair.on_for_rotations(60, 40, 1.06)
    steer_pair.on_for_rotations(0, 20, 0.2)
    lower_motor.on_for_degrees(10, 56)
    grabber_servo.on_for_degrees(10, -90)
    timed_follower(sensor=center_sensor, timemax=0.65, speed=20, kp=0.2, side_of_line=1)
    steer_pair.off()
    lower_motor.on_for_degrees(10, -75)
