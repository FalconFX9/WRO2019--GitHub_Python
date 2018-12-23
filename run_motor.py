from ev3dev.auto import *
import time

mA = Motor(OUTPUT_A)
cl = ColorSensor('in2')

while True:
    print(cl.reflected_light_intensity)
    sleep(1)
