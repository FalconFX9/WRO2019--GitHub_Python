from ev3dev2.auto import Sensor, ColorSensor
from abc import ABC, abstractmethod


class SensorDeclaration(ABC):

    def __init__(self, sensor1, sensor2, sensor3, sensor4):
        self.sensor1 = sensor1
        self.sensor2 = sensor2
        self.sensor3 = sensor3
        self.sensor4 = sensor4
        sensor1.mode = 'RGB'
        sensor2.mode = 'RGB'
        sensor3.mode = 'RGB'
        sensor4.mode = 'RGB'
        super().__init__()

    @abstractmethod
    def use_sensors(self):
        self.sensor1 = Sensor('in1:i2cl')
        self.sensor2 = Sensor('in2:i2cl')
        self.sensor3 = Sensor('in3:i2cl')
        self.sensor4 = ColorSensor('in4')
