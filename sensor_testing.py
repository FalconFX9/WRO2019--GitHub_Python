from ev3dev2.auto import *
from time import sleep

timeduration = time.time() + 5

# Defining Sensors

Sensor1 = Sensor('in1')
Sensor2 = Sensor('in2')
Sensor3 = Sensor('in3')
Sensor4 = ColorSensor('in4')

# Setting Sensor mode

Sensor1.mode = 'RGB'
Sensor2.mode = 'RGB'
Sensor3.mode = 'RGB'

# SSH and on Brick Debugging

for x in range(1, 50):
    print(Sensor1.value(3))
    sleep(0.1)

for x in range(1, 50):
    print(Sensor2.value(3))
    sleep(0.1)

for x in range(1, 50):
    print(Sensor3.value(3))
    sleep(0.1)

for x in range(1, 50):
    print(Sensor4.reflected_light_intensity)
    sleep(0.1)
