import datetime as dt
import matplotlib.pyplot as plt
from line_follower_class import *

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
bx = fig.add_subplot(1, 1, 2)
cx = fig.add_subplot(1, 1, 2)
xs = []
ys = []
ys2 = []
ys3 = []
ts = []

# Sample reflected light intensity every 100th of a second for 10 seconds
for t in range(0, 1000):

    # Read reflected light intensity from the color sensors
    sensor_value = center_sensor.reflected_light_intensity

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(sensor_value)
    ys2.append(left_side_sensor.reflected_light_intensity)
    ys3.append(right_side_sensor.reflected_light_intensity)
    ts.append(35)

    # Wait 0.01 second before sampling light intensity again
    sleep(0.01)

# Draw plot
ax.plot(xs, ys)
ax.plot(xs, ts)
bx.plot(xs, ys2)
cx.plot(xs, ys3)

# Format plot
plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.30)
plt.title('Sensor value compared to target')
plt.ylabel('Reflected light intensity %')

# Draw the graph
plt.show()
