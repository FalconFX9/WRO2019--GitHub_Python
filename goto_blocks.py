from line_follower_class import *
import threading
import queue


def check_for_lines(out_que, num_lines):
    count = 0
    while count < num_lines:
        if left_side_sensor.value(3) < 80:
            print(count)
            count = count + 1
            sleep(0.3)
    lines_passed = True
    out_que.put(lines_passed)


def goto_blocks():
    steer_pair.on_for_rotations(20, -20, 0.6)
    print(" This is que.get() : ", que.get())
    while not que.get():
        print(que.get())
        hisp_center_follower(side_of_line=1)
        print(que.get())
    steer_pair.off()


que = queue.Queue(maxsize=0)
t = threading.Thread(target=check_for_lines, args=(que, 4,))
t.setDaemon(True)
t.start()
t.join()
goto_blocks()
