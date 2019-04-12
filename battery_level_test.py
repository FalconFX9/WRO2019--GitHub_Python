#!/usr/bin/env python3


def check_battery():

    battery = open("/sys/devices/platform/battery/power_supply/lego-ev3-battery/voltage_now")
    text = battery.read()
    return int(text)

