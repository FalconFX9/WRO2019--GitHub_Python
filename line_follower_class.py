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
            self.error = self.target - (float(self.__color_sensor.value(3)) / 2)
        else:
            self.error = self.target - float(self.__color_sensor.reflected_light_intensity)
        self.integral = self.error + self.integral
        self.derivative = self.error - self.last_error
        motor_steering = ((self.error * kp) + (self.integral * K_INTEGRAL) + (self.derivative * K_DERIVATIVE)) * float(
            side_of_line)
        self.last_error = self.error
        return motor_steering

    class SideOfLine:
        left = 1
        right = -1


def center_corrector(out_que, out_que2):
    while True:
        follow = OneSensorLineFollower(center_sensor)
        steering = follow.follower(kp=0.15, sensor_type='Stock')
        steering2 = follow.follower(kp=0.3, sensor_type='Stock')
        out_que.put(steering)
        out_que2.put(steering2)
        sleep(0.01)


def left_corrector(out_que, out_que2):
    while True:
        follow = OneSensorLineFollower(left_side_sensor)
        steering = follow.follower(kp=0.15)
        steering2 = follow.follower(kp=0.3)
        out_que.put(steering)
        out_que2.put(steering2)
        sleep(0.01)


def right_corrector(out_que, out_que2):
    while True:
        follow = OneSensorLineFollower(right_side_sensor)
        steering = follow.follower(kp=0.15)
        steering2 = follow.follower(kp=0.3)
        out_que.put(steering)
        out_que2.put(steering2)
        sleep(0.01)


# Initiating threads for all sensors and correction values
que = queue.Queue(maxsize=0)
que2 = queue.Queue(maxsize=0)
que3 = queue.Queue(maxsize=0)
que4 = queue.Queue(maxsize=0)
que5 = queue.Queue(maxsize=0)
que6 = queue.Queue(maxsize=0)
t = threading.Thread(target=center_corrector, args=(que, que2, ))
t.setDaemon(True)
t.start()
t3 = threading.Thread(target=left_corrector, args=(que3, que4, ))
t3.setDaemon(True)
t3.start()
t5 = threading.Thread(target=right_corrector, args=(que5, que6, ))
t5.setDaemon(True)
t5.start()
timemax = time() + 5
while time() < timemax:
    print("First Sensor Value : " + str(que.get()) + str(que2.get()))
    print("Second Sensor Value : " + str(que3.get()) + str(que4.get()))
    print("Third Sensor Value : " + str(que5.get()) + str(que6.get()))


def high_speed_follower(speed=DEFAULT_SPEED):
    steer_pair.on(que2.get(), speed)





