#!/usr/bin/env python3


def check_battery():

    battery = open("/sys/devices/platform/battery/power_supply/lego-ev3-battery/voltage_now")
    for i in range(0, 100):
        text = battery.read()
        print(text)


check_battery()
