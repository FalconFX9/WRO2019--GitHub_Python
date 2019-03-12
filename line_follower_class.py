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

    def follower(self, side_of_line=None, kp=K_PROPORTIONAL, sensor_type='Hitechnic'):
        if side_of_line is None:
            side_of_line = self.SideOfLine.left
        else:
            side_of_line = self.SideOfLine.right
        if sensor_type == 'Hitechnic':
            self.__color_sensor.mode = 'RGB'
            self.error = self.target - (self.__color_sensor.value(3) / 2)
        else:
            self.error = self.target - self.__color_sensor.reflected_light_intensity
        self.integral = self.error + self.integral
        self.derivative = self.error - self.last_error
        motor_steering = ((self.error * kp) + (self.integral * K_INTEGRAL) + (self.derivative * K_DERIVATIVE)) * float(
            side_of_line)
        self.last_error = self.error
        return motor_steering

    class SideOfLine:
        left = 1
        right = -1


def hisp_center_corrector(out_que):
    while True:
        follow = OneSensorLineFollower(center_sensor)
        steering = follow.follower(kp=0.15, sensor_type='Stock')
        out_que.put(steering)
        sleep(0.01)


def losp_center_corrector(out_que):
    while True:
        follow = OneSensorLineFollower(center_sensor)
        steering = follow.follower(kp=0.3)
        out_que.put(steering)
        sleep(0.01)


def hisp_left_corrector(out_que):
    while True:
        follow = OneSensorLineFollower(left_side_sensor)
        steering = follow.follower(kp=0.15)
        out_que.put(steering)
        sleep(0.01)


def losp_left_corrector(out_que):
    while True:
        follow = OneSensorLineFollower(left_side_sensor)
        steering = follow.follower(kp=0.3)
        out_que.put(steering)
        sleep(0.01)


def hisp_right_corrector(out_que):
    while True:
        follow = OneSensorLineFollower(right_side_sensor)
        steering = follow.follower(kp=0.15)
        out_que.put(steering)
        sleep(0.01)


def losp_right_corrector(out_que):
    while True:
        follow = OneSensorLineFollower(right_side_sensor)
        steering = follow.follower(kp=0.3)
        out_que.put(steering)
        sleep(0.01)


# Initiating threads for all sensors and correction values
que = queue.Queue(maxsize=0)
que2 = queue.Queue(maxsize=0)
que3 = queue.Queue(maxsize=0)
que4 = queue.Queue(maxsize=0)
que5 = queue.Queue(maxsize=0)
que6 = queue.Queue(maxsize=0)
t = threading.Thread(target=hisp_center_corrector, args=(que,))
t.setDaemon(True)
t.start()
t2 = threading.Thread(target=losp_center_corrector, args=(que2,))
t2.setDaemon(True)
t2.start()
t3 = threading.Thread(target=hisp_left_corrector, args=(que3,))
t3.setDaemon(True)
t3.start()
t4 = threading.Thread(target=losp_left_corrector, args=(que4,))
t4.setDaemon(True)
t4.start()
t5 = threading.Thread(target=hisp_right_corrector, args=(que5,))
t5.setDaemon(True)
t5.start()
t6 = threading.Thread(target=losp_right_corrector, args=(que6,))
t6.setDaemon(True)
t6.start()
timemax = time() + 5
while time() < timemax:
    print(que.get())
    left_side_sensor.mode = 'COLOR'
    print(left_side_sensor.value())


def high_speed_follower(speed=DEFAULT_SPEED, rotations=5):
    steer_pair.on_for_rotations(que.get(), speed, rotations)





