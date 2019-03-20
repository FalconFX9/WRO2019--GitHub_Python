from sensor_and_motor_startup import *

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

    def __init__(self, color_sensor):
        self.__color_sensor = color_sensor

    def follower(self, side_of_line=None, kp=K_PROPORTIONAL, speed=DEFAULT_SPEED,
                 sensor_target=target):
        if side_of_line is None:
            side_of_line = self.SideOfLine.left
        else:
            side_of_line = self.SideOfLine.right
        self.target = sensor_target
        self.error = self.target - float(self.__color_sensor.reflected_light_intensity)
        self.integral = self.error + self.integral
        self.derivative = self.error - self.last_error
        motor_steering = ((self.error * kp) + (self.integral * K_INTEGRAL) + (self.derivative * K_DERIVATIVE)) * float(
            side_of_line)
        self.last_error = self.error
        print(motor_steering)
        steer_pair.on(motor_steering, -speed)

    class SideOfLine:
        left = 1
        right = -1


def hisp_center_follower(side_of_line=None, speed=DEFAULT_SPEED):
    follow = OneSensorLineFollower(center_sensor)
    follow.follower(side_of_line=side_of_line, kp=0.15, speed=speed)


def losp_center_follower(side_of_line=None, speed=20):
    follow = OneSensorLineFollower(center_sensor)
    follow.follower(side_of_line=side_of_line, kp=0.6, speed=speed)


def hisp_left_follower(side_of_line=None, speed=DEFAULT_SPEED):
    follow = OneSensorLineFollower(left_side_sensor)
    follow.follower(side_of_line=side_of_line, kp=0.15, speed=speed, sensor_target=50)


def losp_left_follower(side_of_line=None, speed=20):
    follow = OneSensorLineFollower(left_side_sensor)
    follow.follower(side_of_line=side_of_line, kp=0.3, speed=speed)


def hisp_right_follower(side_of_line=None, speed=DEFAULT_SPEED):
    follow = OneSensorLineFollower(right_side_sensor)
    follow.follower(side_of_line=side_of_line, kp=0.3, speed=speed, sensor_target=35)


def losp_right_follower(side_of_line=None, speed=20):
    follow = OneSensorLineFollower(right_side_sensor)
    follow.follower(side_of_line=side_of_line, kp=0.7, speed=speed, sensor_target=20)


def timed_follower(sensor, timemax, side_of_line=None, speed=DEFAULT_SPEED):
    follower = OneSensorLineFollower(sensor)
    timemax = time() + timemax
    while time() < timemax:
        follower.follower(side_of_line=side_of_line, kp=0.3, speed=speed, sensor_target=50)


def follow_to_line(following_sensor=center_sensor, line_sensor=center_sensor, speed=DEFAULT_SPEED, side_of_line=None):
    follow = OneSensorLineFollower(following_sensor)
    while line_sensor.reflected_light_intensity > 20:
        follow.follower(side_of_line=side_of_line, kp=0.15, speed=speed, sensor_target=45)


"""
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
    steer_pair.on(que2.get(), -speed)
"""
