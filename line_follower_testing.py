from line_follower_class import *

"""
What this code does is it will run for 5 seconds evey time, but will ask you to change the K_D value after each run.
It will at first ask if you want to do a run with default K_D.
The first run with the option to change the K_D does not have an option to change the K_P, but the runs after will if 
changing K_P was selected at the start.
Feel free to go and try out many different values and combinations
The default K_P is 0.3, while the default K_D is 0.17
"""

if input("Do you also want to change K_P after each run ? (Y/N) ") == 'Y':
    change_kp = True
else:
    change_kp = False

if input("Do a run with default K_D ? (Y/N) ") == 'Y':
    timed_follower(sensor=center_sensor, side_of_line=1, timemax=4, kp=0.3, ttarget=45)
    steer_pair.off()
print('Change K_D to input value')
K_D = float(input('Please enter a new K_D value here : '))
follow_for_xlines(4, sensor=right_side_sensor, side_of_line=1, ttarget=45, kd=K_D)
steer_pair.off()

while True:
    print('Change K_D to input value')
    K_D = float(input('Please enter a new K_D value here : '))
    if change_kp:
        kp = float(input('Enter a new K_P value here : '))
    else:
        kp = 0.3
    follow_for_xlines(4, sensor=right_side_sensor, side_of_line=1, ttarget=45, kp=kp, kd=K_D)
    steer_pair.off()
