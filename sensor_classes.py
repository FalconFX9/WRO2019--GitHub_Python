from ev3dev2.auto import Sensor, ColorSensor, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, MoveSteering
from abc import ABC, abstractmethod


class SensorDeclaration:

    def __init__(self, sensor1, sensor2, sensor3, sensor4):
        self.sensor1 = sensor1
        self.sensor2 = sensor2
        self.sensor3 = sensor3
        self.sensor4 = sensor4
        super().__init__()

    def use_sensors(self):
        self.sensor1 = Sensor('in1:i2cl')
        self.sensor2 = Sensor('in2:i2cl')
        self.sensor3 = Sensor('in3:i2cl')
        self.sensor4 = ColorSensor('in4')
        self.sensor1.mode = 'RGB'
        self.sensor2.mode = 'RGB'
        self.sensor3.mode = 'RGB'


class MotorDeclaration:

    def __init__(self, lm1, lm2, s1, s2, steering):
        self.lm1 = lm1
        self.lm2 = lm2
        self.s1 = s1
        self.s2 = s2
        self.steering = steering

    def use_motors(self):
        self.lm1 = LargeMotor(OUTPUT_B)
        self.lm2 = LargeMotor(OUTPUT_C)
        self.s1 = MediumMotor(OUTPUT_A)
        self.s2 = MediumMotor(OUTPUT_D)
