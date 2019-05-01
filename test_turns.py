from ev3dev2.auto import *

motor = LargeMotor(OUTPUT_C)

motor.on_for_rotations(-60, 5)
