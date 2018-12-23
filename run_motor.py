from ev3dev.auto import *
from time import sleep

mA = Motor(OUTPUT_A)
cl = Sensor('in2')
cl.mode = 'WHITE'
while True:
    print(cl.value())
    sleep(1)
