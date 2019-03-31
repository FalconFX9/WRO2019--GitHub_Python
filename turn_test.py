from line_follower_class import *

file_s = open('sensor_data.txt', 'w+')
file_x = open('time_data.txt', 'w+')
side_color_sensor.mode = 'RGB'
block_is_black = False


def look_at_blocks():
    global block_is_black
    if side_color_sensor.value(3) > 100:
        sleep(0.3)
    elif 100 > side_color_sensor.value(3) > 40:
        block_is_black = True


lower_motor.off(brake=True)
tick = 0
start_time = time()
while not block_is_black:
    hisp_right_follower(speed=20)
    file_s.write(str(side_color_sensor.value(3)) + '\n')
    file_x.write(str(round((time() - start_time), 1)) + '\n')
steer_pair.off()

file_s.close()
file_x.close()


def turn_and_pick_up():
    lower_motor.on_for_degrees(10, -10)
    steer_pair.on_for_rotations(60, 40, 1.06)
    steer_pair.on_for_rotations(0, 20, 0.2)
    lower_motor.on_for_degrees(10, 56)
    grabber_servo.on_for_degrees(10, -90)
    timed_follower(sensor=center_sensor, timemax=0.65, speed=20, kp=0.2, side_of_line=1)
    steer_pair.off()
    lower_motor.on_for_degrees(10, -75)
