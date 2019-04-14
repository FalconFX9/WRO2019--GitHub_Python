from sensor_and_motor_startup import *

while True:
    turn_rotations = float(input('Enter new number of rotations here: '))
    steer_pair.on_for_rotations(-70, -40, turn_rotations)
