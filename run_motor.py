from ev3dev2.auto import *
from time import sleep

mA = Motor(OUTPUT_A)
cl = Sensor('in2:i2c1')
cl.mode('WHITE')
while True:
    print(cl.value())
    sleep(1)
