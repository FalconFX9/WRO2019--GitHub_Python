from line_follower_class import *

side_color_sensor.mode = 'RGB'


def pick_up_block():
    lower_motor.off()
    while not 100 > side_color_sensor.value(3) > 40:
        hisp_right_follower(speed=40, kp=0.15)
        print(side_color_sensor.value(3))
    steer_pair.off()
    timed_follower(sensor=right_side_sensor, speed=30, kp=0.15, timemax=0.33)
    lower_motor.on_for_degrees(10, -10)
    steer_pair.on_for_rotations(60, 40, 1.2)
    steer_pair.on_for_rotations(0, 20, 0.2)
    lower_motor.on_for_degrees(10, 56)
    sleep(0.2)
    timed_follower(sensor=center_sensor, timemax=0.85, speed=20, kp=0.35)
    steer_pair.off()
    lower_motor.on_for_degrees(10, -52)


lower_motor.off()
while True:
    try:
        hisp_right_follower(speed=40)
        file_s.write(str(side_color_sensor.value(3)))
        file_x.write(str(round((time()), 1)) + '\n')
    except KeyboardInterrupt:
        file_s.close()
        file_x.close()
