from enum import Enum
from ev3dev2.auto import *

DEFAULT_SPEED = 60

# PID Values --These are subjective and need to be tuned to the robot and mat
# Kp must be augmented or decreased until the robot follows the line smoothly --Higher Kp = Stronger corrections
# Same with Ki, after Kp is done --- note, Ki is not used in this case (error accumulation)
# Kd to 1, and move up or done until smooth, after Kp and Ki
# This process can take a VERY long time to fine-tune
KP = 0.83
K_INTEGRAL = 0
K_DERIVATIVE = 0.002


class SingleLineFollower:
    """
    Line follow that uses one sensor at a time to follow a line.
    """

    __error = 0
    __target = 0
    __integral = 0
    __last_error = 0
    __derivative = 0

    def __init__(self, color_sensor_gauche, color_sensor_droite, move_steerer):
        self.__color_sensor_left = color_sensor_gauche
        self.__color_sensor_right = color_sensor_droite
        self.__move_steerer = move_steerer

    def follow(self, side=None, speed=DEFAULT_SPEED):
        if None:
            side = self.FollowSide.left

        if side == self.FollowSide.left:
            self.__error = self.__target - (self.__color_sensor_left.value(3) / 2)
        else:
            self.__error = self.__target - (self.__color_sensor_right.value(3) / 2)

        self.__integral = self.__error + self.__integral
        self.__derivative = self.__error - self.__last_error
        motor_steering = ((self.__error * KP) + (self.__integral * K_INTEGRAL) + (
                self.__derivative * K_DERIVATIVE)) * side.value

        self.__move_steerer.on(motor_steering, -speed)
        self.__last_error = self.__error

    class FollowSide(Enum):
        """Enum for which side of the line to follow."""
        left = 0
        right = 1


def _single_line_follower_test():
    line_follower = SingleLineFollower(Sensor('in2:i2c1'), Sensor('in3:i2c1'), MoveSteering(OUTPUT_A, OUTPUT_B))

    while True:
        line_follower.follow()


if __name__ == "__main__":
    # Single line follower test
    _single_line_follower_test()
