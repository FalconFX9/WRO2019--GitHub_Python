import datetime as dt
import matplotlib.pyplot as plt
from time import sleep

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
ts = []

# Sample reflected light intensity every 100th of a second for 10 seconds
for t in range(0, 1000):

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(t)
    ts.append(35)

    # Wait 0.01 second before sampling light intensity again
    sleep(0.01)

# Draw plot
ax.plot(xs, ys)
ax.plot(xs, ts)

# Format plot
plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.30)
plt.title('Sensor value compared to target')
plt.ylabel('Reflected light intensity %')

# Draw the graph
plt.show()
