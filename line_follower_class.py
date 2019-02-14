from enum import Enum

DEFAULT_SPEED = 60

# PID Values --These are subjective and need to be tuned to the robot and mat
# Kp must be augmented or decreased until the robot follows the line smoothly --Higher Kp = Stronger corrections
# Same with Ki, after Kp is done --- note, Ki is not used in this case (error accumulation)
# Kd to 1, and move up or done until smooth, after Kp and Ki
# This process can take a VERY long time to fine-tune
K_PROPORTIONAL = 0.2
K_INTEGRAL = 0
K_DERIVATIVE = 0


class OneSensorLineFollower:
    target = 35
    error = 0
    last_error = 0
    derivative = 0
    integral = 0

    def __init__(self, color_sensor, move_steering):
        self.__color_sensor = color_sensor
        self.__move_steering = move_steering

    def follower(self, side_of_line=None, speed=DEFAULT_SPEED):
        if None:
            side_of_line = self.SideOfLine.left
        self.error = self.target - (self.__color_sensor.value(3) / 2)
        self.integral = self.error + self.integral
        self.derivative = self.error - self.last_error
        motor_steering = ((self.error * K_PROPORTIONAL) + (self.integral * K_INTEGRAL) + (self.derivative * K_DERIVATIVE
                                                                                          )) * int(side_of_line)
        self.__move_steering.on(motor_steering, -speed)
        self.last_error = self.error

    class SideOfLine(Enum):
        left = 0
        right = 1
