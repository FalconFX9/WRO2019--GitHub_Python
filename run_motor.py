from ev3dev.auto import *
import time

mA = Motor(OUTPUT_A)
cl = ColorSensor('in2')

if cl.reflected_light_intensity < 40:
    mA.run_forever()
else:
    mA.stop()
