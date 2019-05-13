from line_follower_class import *
from threading import Thread


file_x = open('time_data.txt', 'w+')
file_s = open('sensor_data.txt', 'w+')
side_color_sensor.mode = 'RGB'
block_is_black = False
start_time = time()


def look_at_blocks():
    global block_is_black
    while not block_is_black:
        print(side_color_sensor.value(3))
        if side_color_sensor.value(3) > 120:
            sleep(0.3)
        elif 120 > side_color_sensor.value(3) > 40:
            block_is_black = True


Thread(target=look_at_blocks).start()
while not block_is_black:
    hisp_right_follower(speed=30)
steer_pair.off()
