from line_follower_class import *
from threading import Thread


file_x = open('time_data.txt', 'w+')
file_s = open('sensor_data.txt', 'w+')
side_color_sensor.mode = 'RGB'
block_is_black = False
start_time = time()


def look_at_blocks():
    global block_is_black
    while True:
        while not block_is_black:
            print(side_color_sensor.value(3))
            if side_color_sensor.value(3) > 100:
                sleep(0.3)
            elif 100 > side_color_sensor.value(3) > 40:
                block_is_black = True
        try:
            print(side_color_sensor.value(3))
            file_x.write(str(side_color_sensor.value(3)) + '\n')
            file_s.write(str(round((time() - start_time), 1)) + '\n')
        except KeyboardInterrupt:
            file_x.close()
            file_s.close()
            break


Thread(target=look_at_blocks).start()
while True:
    try:
        hisp_right_follower(speed=30)
    except KeyboardInterrupt:
        steer_pair.off()
        file_s.close()
        file_x.close()
        break
