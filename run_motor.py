from ev3dev2.auto import *
from time import sleep

cl = Sensor('in2:i2c1')
cl.mode = 'RGB'
for x in range(100):
    print(cl.value(3))
