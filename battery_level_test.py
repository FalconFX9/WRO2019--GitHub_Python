def get_battery_percentage():
    """
    Return an int() of the percentage of battery life remaining
    """
    voltage_max = None
    voltage_min = None
    voltage_now = None

    with open('/sys/devices/platform/legoev3-battery/power_supply/legoev3-battery/uevent', 'r') as fh:
        for line in fh:

            if not voltage_max:
                re_voltage_max = re.search(
                    'POWER_SUPPLY_VOLTAGE_MAX_DESIGN=(\d+)', line)

                if re_voltage_max:
                    voltage_max = int(re_voltage_max.group(1))
                    continue

            if not voltage_min:
                re_voltage_min = re.search(
                    'POWER_SUPPLY_VOLTAGE_MIN_DESIGN=(\d+)', line)

                if re_voltage_min:
                    voltage_min = int(re_voltage_min.group(1))
                    continue

            if not voltage_now:
                re_voltage_now = re.search(
                    'POWER_SUPPLY_VOLTAGE_NOW=(\d+)', line)

                if re_voltage_now:
                    voltage_now = int(re_voltage_now.group(1))

            if re_voltage_max and re_voltage_min and re_voltage_now:
                break

    if voltage_max and voltage_min and voltage_now:

        # This happens with the EV3 rechargeable battery if it is fully charge
        if voltage_now >= voltage_max:
            return 100

        # Haven't seen this scenario but it can't hurt to check for it
        elif voltage_now <= voltage_min:
            return 0

        # voltage_now is between the min and max
        else:
            voltage_max -= voltage_min
            voltage_now -= voltage_min
            return int(voltage_now / float(voltage_max) * 100)
    else:
        logger.error('voltage_max %s, voltage_min %s, voltage_now %s' %
                     (voltage_max, voltage_min, voltage_now))
        return 0


for i in range(0, 100):
    print(get_battery_percentage())
