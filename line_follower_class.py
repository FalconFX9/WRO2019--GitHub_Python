from sensor_and_motor_startup import *
import threading
import queue

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
    target = 24
    error = 0
    last_error = 0
    derivative = 0
    integral = 0

    def __init__(self, color_sensor):
        self.__color_sensor = color_sensor

    def follower(self, side_of_line=None, kp=K_PROPORTIONAL):
        if side_of_line is None:
            side_of_line = self.SideOfLine.left
        else:
            side_of_line = self.SideOfLine.right
        self.error = self.target - (self.__color_sensor.value(3) / 2)
        self.integral = self.error + self.integral
        self.derivative = self.error - self.last_error
        motor_steering = ((self.error * kp) + (self.integral * K_INTEGRAL) + (self.derivative * K_DERIVATIVE
                                                                                          )) * float(side_of_line)
        self.last_error = self.error
        return motor_steering

    class SideOfLine:
        left = 1
        right = -1


def hisp_center_corrector(out_que):
    follow = OneSensorLineFollower(left_side_sensor)
    while True:
        steering = follow.follower(kp=0.15)
        out_que.put(steering)


def low_speed_follower(speed=DEFAULT_SPEED, rotations=5):
    follower = OneSensorLineFollower(center_sensor)
    steer_pair.on_for_rotations(follower.follower(kp=0.3), speed, rotations)


que = queue.Queue()
t = threading.Thread(target=hisp_center_corrector(que))
t.start()
t.join()
print(que.get())






