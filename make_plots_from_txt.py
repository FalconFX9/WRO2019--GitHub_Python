import matplotlib
import matplotlib.pyplot as plt

"""
HOW TO TUNE PD CONTROLLER ACCORDING TO ZIERGLER-NICHOLLS METHOD
Start to increase P from 0 until robot oscillates consistently
Value of P when robots starts to oscillate consistently is ultimate gain, or Ku
Kp should then be 0.8Ku
Look at graph and take oscillation period, this is Tu
Kd should be Ku*Tu/10
"""
matplotlib.use('Qt5Agg')
file_s = open('sensor_data.txt', 'r')
file_st = open('steering_data.txt', 'r')
file_x = open('time_data.txt', 'r')
x = []
y = []
t = []
st = []
target = 40
plt.subplot(2, 1, 1)
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

plt.subplot(2, 1, 2)
t.clear()
for i in file_st:
    st.append(float(i))
    t.append(0)
for i in file_x:
    x.append(i)
for p in range(0, len(y)):
    plt.plot(x, st)
    plt.plot(x, t)
plt.title('Target is ' + str(0) + ' (blue line).')
plt.ylim(-20, 20)

plt.show()
