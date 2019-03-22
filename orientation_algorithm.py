colorblock = []
position = {}
colorblock.append(3)
colorblock.append(7)
colorblock.append(4)
colorblock.append(5)
for i in range(0, 4):
    print(colorblock[i])
    if colorblock[i] == 4:
        position['Green'] = i * 90
    elif colorblock[i] == 5:
        position['Yellow'] = i * 90
    elif colorblock[i] == 3:
        position['Blue'] = i * 90
    elif colorblock[i] == 7:
        position['Red'] = i * 90

print(position)
