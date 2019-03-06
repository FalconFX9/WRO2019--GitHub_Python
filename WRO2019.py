#!/usr/bin/env python3
from ev3dev2.auto import Button
from regrouped_functions import wro2019
from start_sequence import *
from threading import *

btn = Button()

t = Thread(wro2019())
t.setDaemon(True)
t.start()

while not btn.any():
    pass

steer_pair.off()
quit()
