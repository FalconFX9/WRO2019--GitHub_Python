from enum import Enum
from ev3dev2.auto import *
from sensor_classes import SensorDeclaration, MotorDeclaration

DEFAULT_SPEED = 60

# PID Values --These are subjective and need to be tuned to the robot and mat
# Kp must be augmented or decreased until the robot follows the line smoothly --Higher Kp = Stronger corrections
# Same with Ki, after Kp is done --- note, Ki is not used in this case (error accumulation)
# Kd to 1, and move up or done until smooth, after Kp and Ki
# This process can take a VERY long time to fine-tune
KP = 0.83
K_INTEGRAL = 0
K_DERIVATIVE = 0.002
sensor3 = Sensor('in3:i2c1')
sensor3.mode = 'RGB'


class SingleLineFollower:
    """
    Line follow that uses one sensor at a time to follow a line.
    """

    __error = 0
    __target = 0
    __integral = 0
    __last_error = 0
    __derivative = 0

    def __init__(self, __color_sensor_gauche, __color_sensor_droit, move_steerer):
        self.__color_sensor_left = __color_sensor_gaucheputt
        self.__color_sensor_right = __color_sensor_droit
        __color_sensor_droit = Sensor('in2:i2c1')
        __color_sensor_gauche = Sensor('in1:i2c1')
        self.__move_steerer = move_steerer

    def follow(self, side=None, side_of_line=None, speed=DEFAULT_SPEED):
        if None:
            side = self.FollowSide.left
            side_of_line = self.FollowSide.left

        if side == self.FollowSide.left:
            self.__error = self.__target - (self.__color_sensor_left.value(3) / 2)
        else:
            self.__error = self.__target - (self.__color_sensor_right.value(3) / 2)

        self.__integral = self.__error + self.__integral
        self.__derivative = self.__error - self.__last_error
        motor_steering = ((self.__error * KP) + (self.__integral * K_INTEGRAL) + (
                self.__derivative * K_DERIVATIVE)) * side_of_line

        self.__move_steerer.on(motor_steering, -speed)
        self.__last_error = self.__error

    class FollowSide(Enum):
        """Enum for which side of the line to follow."""
        left = 0
        right = 1


def _single_line_follower_test():
    line_follower = SingleLineFollower(MoveSteering(OUTPUT_A, OUTPUT_B))

    while sensor3.value(3) > 30:
        line_follower.follow()


if __name__ == "__main__":
    # Single line follower test
    _single_line_follower_test()


def _line_follower_to_next_line(side, side_of_line, speed=DEFAULT_SPEED):
    line_follower = SingleLineFollower(MoveSteering(OUTPUT_B, OUTPUT_C))
    while not SensorDeclaration.sensor3.value(3) > 30:
        line_follower.follow(side=side, side_of_line=side_of_line, speed=speed)


def _line_follower_to_color(side=1, side_of_line=1, speed=DEFAULT_SPEED):
    line_follower = SingleLineFollower(MoveSteering(OUTPUT_B, OUTPUT_C))
    SensorDeclaration.sensor3.mode = 'RGB'
    while not SensorDeclaration.sensor3.value > 40 or SensorDeclaration.sensor3.value == 4 or \
            SensorDeclaration.sensor3.value == 6 or SensorDeclaration.sensor3.value == 8:
        line_follower.follow(side=side, side_of_line=side_of_line, speed=speed)
