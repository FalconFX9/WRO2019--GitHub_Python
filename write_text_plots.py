from time import *
from random import *

file_s = open('sensor_data.txt', 'w+')
file_x = open('time_data.txt', 'w+')
log = True


def write_to_file():
    starttime = time()
    for i in range(0, 100):
        file_s.write(str(randint(30, 40)) + '\n')
        file_x.write(str(round((time() - starttime), 1)) + '\n')
        sleep(0.1)


write_to_file()
file_x.close()
file_s.close()
