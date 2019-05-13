from line_follower_class import *
from threading import Thread


file_x = open('time_data.txt', 'w+')
file_s = open('sensor_data.txt', 'w+')
side_color_sensor.mode = 'RGB'
block_is_black = False


def look_at_blocks():
    global block_is_black
    while not block_is_black:
        print(side_color_sensor.value())
        if side_color_sensor.value(3) > 100:
            sleep(0.3)
        elif 100 > side_color_sensor.value(3) > 40:
            block_is_black = True
    print('Thread look_at_blocks is finished')


Thread(target=look_at_blocks).start()
while True:
    try:
        while not block_is_black:
            hisp_right_follower(speed=40)
        print(side_color_sensor.value(3))
        file_x.write(str(side_color_sensor.value(3)))
        file_s.write(str(round(time(), 1)))
    except KeyboardInterrupt:
        steer_pair.off()
        file_s.close()
        file_x.close()
