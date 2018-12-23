from ev3dev.auto import *
import time

mA = Motor(OUTPUT_A)
cl = ColorSensor('in2')
cl.mode = 'WHITE'

if cl.value < 40:
    mA.run_forever()
else:
    mA.stop()
