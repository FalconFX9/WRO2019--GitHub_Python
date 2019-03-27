from line_follower_class import *

lower_motor.off()
steer_pair.on_for_rotations(-50, 40, 0.6)
steer_pair.on_for_rotations(50, -40, 0.8)
