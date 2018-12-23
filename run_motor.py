from ev3dev.auto import *
from time import sleep

mA = Motor(OUTPUT_A)
cl = Sensor('in2')

while True:
    print(cl.white)
    sleep(1)
