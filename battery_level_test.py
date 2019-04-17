#!/usr/bin/env python3


def check_battery():

    battery = open("/sys/devices/platform/battery/power_supply/lego-ev3-battery/voltage_now")
    text = battery.read()
    return int(text) / 1000000


def better_compensation():
    extra_power = 8.2
    return (extra_power - check_battery()) * 5
