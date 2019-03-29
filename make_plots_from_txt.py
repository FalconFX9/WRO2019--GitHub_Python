import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')
file_s = open('sensor_data.txt', 'r')
file_x = open('time_data.txt', 'r')
x = []
y = []
t = []
target = 35

for i in file_s:
    y.append(int(i))
for i in file_x:
    x.append(i)
    t.append(target)
for p in range(0, len(y)):
    plt.plot(x, y)
    plt.plot(x, t)
plt.title('Target is ' + str(target) + ' (blue line).')
plt.ylim(0, 100)
plt.show()
