from time import sleep

blocks = []
white_blocks_seen = 0
pick_up_block = False


def first_scan():
    global blocks, white_blocks_seen

    def blocks_list():
        if int(input('Give input')) == 17:
            blocks.append(False)
        else:
            blocks.append(True)
        sleep(1)

    while not len(blocks) == 3:
        blocks_list()
        pass

    for i in range(0, len(blocks)):
        print(blocks[i])
        if not blocks[i]:
            white_blocks_seen += 1

    if white_blocks_seen == 2:
        blocks.append(True)
        blocks.append(True)
        blocks.append(True)


def second_scan():
    global white_blocks_seen, pick_up_block
    while len(blocks) < 6:
        if white_blocks_seen < 2:
            if not int(input('Give value')) == 17:
                blocks.append(True)
                # Go pick up the block
            else:
                blocks.append(False)
            for i in range(0, len(blocks)):
                if not blocks[i]:
                    white_blocks_seen += 1
        else:
            print("All white blocks have been seen")
            # Go pick up all the next blocks


def pick_up_blocks():
    global pick_up_block
    count = 0
    if blocks[count]:
        # Code to pick up the block
        pass
    else:
        # Follow to next line
        pass
    count += 1


first_scan()
second_scan()
