from ev3dev.auto import *
import time

mA = Motor(OUTPUT_A)
cl = ColorSensor('in2')

while True:
    Print(cl.reflected_light_intensity)
    Sleep(1)
