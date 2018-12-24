from ev3dev2.auto import *
from time import sleep

Target = 50
Kp = 0
Ki = 0
Kd = 0

# Sensor declaration

Hitechnic1 = Sensor('in2:i2c1')
Hitechnic1.mode = 'RGB'
Hitechnic2 = Sensor('in3:i2c1')
Hitechnic2.mode = 'RGB'

# Motor Declaration

steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)

# PID Line Follower (1 sensor)


def pidlinefollower(sensor=Hitechnic1):

    print(sensor)
#    target2 = Target - sensor.value(3)
#   steer_pair.run_forever(steering=target2*Kp, speed=100)
    return


pidlinefollower(sensor=Hitechnic1)
sleep(5)
pidlinefollower(sensor=Hitechnic2)


