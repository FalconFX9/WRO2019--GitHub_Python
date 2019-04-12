#!/usr/bin/env python3


def check_battery():

    battery = open("/sys/devices/platform/battery/power_supply/lego_ev3_battery/voltage_now")
    for i in range(0, 100):
        print(battery.read())
