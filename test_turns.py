from ev3dev2.auto import *

steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
steer_pair.on_for_rotations(100, 40, 2)
