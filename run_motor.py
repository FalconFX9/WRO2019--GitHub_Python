from ev3dev2.auto import *
from time import sleep

mA = Motor(OUTPUT_A)
cl = Sensor('in2:i2c1')
while True:
    print(cl.rgb[3])
