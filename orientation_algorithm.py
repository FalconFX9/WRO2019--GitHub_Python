colorblock = []
position = {}
color_names = {0: 'Green', 1: 'Yellow', 2: 'Blue', 3: 'Red'}
colorblock.append(4)
colorblock.append(5)
colorblock.append(7)
colorblock.append(3)
side_of_line = []
sensor = []
offset = []
blocks_down = 0

"""
Positions are as such :

0 :  | 
     |
   _ _ _
    
    
90 : |
     | - -
     |
     
180 : _ _ _
        |
        |
       
270 :      |
       - - |
           |
"""

for i in range(0, 4):
    if colorblock[i] == 4:
        position['Green'] = i * 90
    elif colorblock[i] == 5:
        position['Yellow'] = i * 90
    elif colorblock[i] == 3:
        position['Blue'] = i * 90
    elif colorblock[i] == 7:
        position['Red'] = i * 90


def show_color_assignment():
    for x in range(0, 4):
        if position[color_names[x]] == 0:
            # grabber_servo.on_for_degrees(90, 40)
            # follow appropriate amount
            print(color_names[x] + ' is in position ' + str(position[color_names[x]]))
            pass
        elif position[color_names[x]] == 90:
            print(color_names[x] + ' is in position ' + str(position[color_names[x]]))
            pass
        elif position[color_names[x]] == 180:
            print(color_names[x] + ' is in position ' + str(position[color_names[x]]))
        elif position[color_names[x]] == 270:
            print(color_names[x] + ' is in position ' + str(position[color_names[x]]))


def put_down_all():
    for x in range(0, 4):
        if position[color_names[x]] == 270:
            side_of_line.append('right')
            sensor.append('left')
            offset.append('right')
        elif position[color_names[x]] == 0:
            side_of_line.append('right')
            sensor.append('center')
            offset.append('forward')
        elif position[color_names[x]] == 90:
            side_of_line.append(None)
            sensor.append('right')
            offset.append('left')
        else:
            side_of_line.append('right')
            sensor.append('center')
            offset.append('back')
    print(side_of_line)
    print(sensor)
    print(offset)


def robot_path():
    global blocks_down
    blocks_down += 1
    if offset[blocks_down] == 'right':
        # Turn robot to the right until leftmost sensor senses the line
        pass
    elif offset[blocks_down] == 'left':
        # Turn robot to the left until leftmost sensor senses the line
        pass
    elif offset[blocks_down] == 'forward':
        # Make the robot go forward a bit more
        pass
    else:
        # Make the robot go back a bit
        pass
    # timed_follower(sensor=sensor[blocks_down], timemax=1, side_of_line=side_of_line[blocks_down], speed=30, kp=0.3)


show_color_assignment()
put_down_all()
