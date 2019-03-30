from sensor_and_motor_startup import *

file_s = open('sensor_data.txt', 'w+')
file_st = open('steering_data.txt', 'w+')
file_x = open('time_data.txt', 'w+')
log_to_files = True

DEFAULT_SPEED = 60

# PID Values --These are subjective and need to be tuned to the robot and mat
# Kp must be augmented or decreased until the robot follows the line smoothly --Higher Kp = Stronger corrections
# Same with Ki, after Kp is done --- note, Ki is not used in this case (error accumulation)
# Kd to 1, and move up or done until smooth, after Kp and Ki
# This process can take a VERY long time to fine-tune
K_PROPORTIONAL = 0.2
K_INTEGRAL = 0
K_DERIVATIVE = 0.17


class OneSensorLineFollower:
    target = 35
    error = 0
    last_error = 0
    derivative = 0
    integral = 0
    start_time = time()

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
        steer_pair.on(motor_steering, -speed)
        if log_to_files:
            file_s.write(str(self.__color_sensor.reflected_light_intensity) + '\n')
            file_x.write(str(round((time() - self.start_time), 1)) + '\n')
            file_st.write(str(motor_steering) + '\n')
        else:
            file_st.close()
            file_x.close()
            file_s.close()

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
    follow.follower(side_of_line=side_of_line, kp=0.4, speed=speed, sensor_target=45)


def hisp_right_follower(side_of_line=None, speed=DEFAULT_SPEED):
    follow = OneSensorLineFollower(right_side_sensor)
    follow.follower(side_of_line=side_of_line, kp=0.15, speed=speed, sensor_target=40)


def losp_right_follower(side_of_line=None, speed=20):
    follow = OneSensorLineFollower(right_side_sensor)
    follow.follower(side_of_line=side_of_line, kp=0.3, speed=speed, sensor_target=30)


def timed_follower(sensor, timemax, side_of_line=None, speed=DEFAULT_SPEED, kp=0.15, ttarget=35):
    follower = OneSensorLineFollower(sensor)
    timemax = time() + timemax
    while time() < timemax:
        follower.follower(side_of_line=side_of_line, kp=kp, speed=speed, sensor_target=ttarget)


def follow_to_line(following_sensor=center_sensor, line_sensor=center_sensor, speed=DEFAULT_SPEED, side_of_line=None,
                   kp=0.25):
    follow = OneSensorLineFollower(following_sensor)
    while line_sensor.reflected_light_intensity > 20:
        follow.follower(side_of_line=side_of_line, kp=kp, speed=speed, sensor_target=45)
