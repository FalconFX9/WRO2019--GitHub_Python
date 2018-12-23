from ev3dev.auto import *
import time

mA = Motor(OUTPUT_A)
cl = Sensor(address='in2:i2c1', driver_name='ht-nxt-color-v2')
cl.mode = 'NORM', 'value3'

if cl.value < 40:
    mA.run_forever()
else:
    mA.stop()
