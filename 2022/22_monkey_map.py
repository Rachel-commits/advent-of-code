"""
Advent of Code 2022
Day 22: Monkey Map
Calculate the monkey password given the end position
https://adventofcode.com/2022/day/22
"""

import re

def read_in_file(filename ):
    """
    Read in the file. Create the Wall and tile sets and
    instruction list
    """
    with open(filename, encoding='UTF8') as file:
        x_max = 0
        y_max = 0
        line_num = 0
        start_pos = ()
        tiles = set()
        walls = set()
        instructions = []
        get_instruction = False

        for line in file:
            line_num +=1
            line = line.replace('\n','')

            # Blank Line then stop reading in map
            if not line.strip():
                get_instruction = True

            # read in map
            elif get_instruction is False:
                if line_num> y_max:
                    y_max = line_num
                for pos, element in enumerate (line):
                    pos+=1
                    if element == '.':
                        if not tiles:
                            start_pos = (pos,line_num)
                        tiles.add((pos,line_num))
                    elif element == '#':
                        walls.add((pos,line_num))
                    if pos>x_max:
                        x_max = pos

            elif get_instruction:
                instructions = re.findall(r"[^\W\d_]+|\d+",line)

    return start_pos, tiles, walls, x_max,y_max, instructions

def check_pos_and_move(direction, pos,temp_pos, tiles, walls, x_max,y_max, is_part2):
    """
    Given the new position check if can move and move to new position if able.
    """
    # only used for part 2
    new_dir  = direction

    # If can move then update the new position
    if temp_pos in tiles:
        action = 'move'
        pos = temp_pos

    # If blocked position is unchanged and return blocked
    elif temp_pos in walls:
        action = 'blocked'

    # For wrapping check the wrapped position
    else:
        if is_part2 is False:
            coord, action = wrap_check(direction, temp_pos, tiles, walls, x_max,y_max)
            # If blocked position is unchanged and return blocked
            # If possible move to the wrapped tile update the position
            if action == 'move':
                pos = coord


        # PART2
        elif is_part2:
            coord, action, pt2_new_dir = wrap_check_part2(direction, temp_pos, tiles, walls)
            if action == 'move':
                pos = coord
                new_dir = pt2_new_dir

    return pos, action, new_dir

def wrap_check_part2(direction, temp_pos, tiles, walls):
    """
    For part 2 work out the new wrap position, new direction
    and check if blocked.
    """

    x = temp_pos[0]
    y = temp_pos[1]
    action = ''

    ##check wrap coords after right_edge
    if direction == 0:
        if y <=50:
            new_dir = 2
            new_pos= (100, 151-y)

        elif y<= 100:
            new_dir = 3
            new_pos= (y+50, 50)

        elif y<= 150:
            new_dir = 2
            new_pos= (150, 151-y)

        elif y<=200:
            new_dir = 3
            new_pos= (y-100, 150)

    ## left
    elif direction == 2:
        if y <=50:
            new_dir = 0
            new_pos= (1, 151-y)

        elif y<= 100:
            new_dir = 1
            new_pos= (y-50, 101)

        elif y<= 150:
            new_dir = 0
            new_pos= (51, 151-y)

        elif y<=200:
            new_dir = 1
            new_pos= (y-100, 1)

    ## up
    elif direction == 3:
        if x <=50:
            new_dir = 0
            new_pos= (51, 50+x)

        elif x <=100:
            new_dir = 0
            new_pos= (1, 100+x)

        elif x <=150:
            new_dir = 3
            new_pos= (x-100, 200)

    # down
    elif direction == 1:
        if x <=50:
            new_dir = 1
            new_pos= (x+100, 1)

        elif x <=100:
            new_dir = 2
            new_pos= (50, 100+x)

        elif x <=150:
            new_dir = 2
            new_pos= (100, x-50)

    if new_pos in tiles:
        action = 'move'
    elif new_pos in walls:
        action = 'blocked'

    return new_pos, action, new_dir


def wrap_check(direction, temp_pos,tiles, walls, x_max,y_max):
    """
    For part 1 work out the wrap position and check of blocked
    """
    ## check  x coords from left
    if direction == 0:
        for i in range(x_max):
            i+=1
            if (i,temp_pos[1]) in tiles:
                return (i,temp_pos[1]) ,'move'
            elif (i,temp_pos[1]) in walls:
                return (i,temp_pos[1]) , 'blocked'

    # check y coords from above
    elif direction == 1:
        for i in range(y_max):
            i+=1
            if (temp_pos[0], i) in tiles:
                return (temp_pos[0], i)  ,'move'
            elif (temp_pos[0], i)  in walls:
                return (temp_pos[0], i)  , 'blocked'

    ## check  x coords from right
    elif direction == 2:
        for i in range(x_max):
            if (x_max -i,temp_pos[1]) in tiles:
                return (x_max -i,temp_pos[1]) ,'move'
            elif (x_max -i,temp_pos[1]) in walls:
                return (x_max -i,temp_pos[1]) , 'blocked'

    ## check  y coords from bottom
    elif direction == 3:
        for i in range(y_max):
            if (temp_pos[0], y_max -i) in tiles:
                return (temp_pos[0], y_max -i) ,'move'
            elif (temp_pos[0], y_max -i) in walls:
                return (temp_pos[0], y_max -i) , 'blocked'


def carry_out_instruction(instr,direction, pos,tiles,walls, x_max,y_max, is_part2):
    """
    Given a move number carry out the move, moving by 1 position each time in the given direction
    """
    for _ in range(instr):
        #right
        if direction == 0:
            temp_pos = (pos[0]+1, pos[1])
        #down
        elif direction == 1:
            temp_pos = (pos[0], pos[1] + 1)
        #left
        elif direction == 2:
            temp_pos = (pos[0]-1, pos[1])
        #up
        elif direction ==3:
            temp_pos = (pos[0], pos[1]-1)

        pos, action, direction = check_pos_and_move(direction,
                                                    pos,
                                                    temp_pos,
                                                    tiles,
                                                    walls,
                                                    x_max,
                                                    y_max,
                                                    is_part2)

        if action == 'blocked':
            break
        else:
            continue

    return pos, direction


# Now get the instructions
def process_all_instruction(instructions, pos, tiles, walls, x_max,y_max, is_part2 ):
    """
    Loop through  the instruction list p calcualting the direction and
    then completing the move
    """
    direction = 0
    for instr in instructions:

        if instr.isalpha():
            if instr == 'R':
                direction +=1
            elif instr == 'L':
                direction -=1

            direction = direction % 4

        # Move if possible
        else:
            pos, direction = carry_out_instruction(int(instr),
                                                    direction,
                                                    pos,
                                                    tiles,
                                                    walls,
                                                    x_max,
                                                    y_max,
                                                    is_part2)

    return pos, direction


def run_puzzle():
    """
    Function to output Part 1 and Part 2
    """
    # Part 1
    start_pos, tiles, walls, x_max,y_max, instructions = read_in_file(r'data\day22.txt')
    pos, direction = process_all_instruction(instructions,
                                            start_pos,
                                            tiles,
                                            walls,
                                            x_max,
                                            y_max,
                                            False)
    answer = 1000*pos[1] + 4*pos[0] + direction
    print("The answer to part 1 is ", answer)

    # Part 2
    pos, direction = process_all_instruction(instructions,
                                            start_pos,
                                            tiles,
                                            walls,
                                            x_max,
                                            y_max,
                                            True)
    answer = 1000*pos[1] + 4*pos[0] + direction
    print("The answer to part 2 is ", answer)

run_puzzle()
