from ev3dev2.auto import *
from line_follower_class import *

steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
steer_pair.on_for_rotations(100, 40, 1)
while not center_sensor.reflected_light_intensity < 30:
    steer_pair.on(100, 40)
steer_pair.off()
