from ev3dev.auto import *
import time

mA = Motor(OUTPUT_A)
cl = Sensor(address='in2:i2c')
cl.mode = 'white'

if cl.value < 40:
    mA.run_forever()
else:
    mA.stop()

mA.stop(stop_action='brake')