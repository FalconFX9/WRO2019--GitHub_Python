#!/usr/bin/env python3
from PID_Line_Follower import *
from threading import *

btn = Button()

t = Thread(wro2019())
t.setDaemon(True)
t.start()

while not btn.any():
    pass

quit()
