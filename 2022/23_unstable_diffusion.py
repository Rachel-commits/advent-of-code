"""
Advent of Code 2022
Day 23: Unstable Diffusion
Calculate the number of empty squares after
10 rounds and the first round that no elf can move.
https://adventofcode.com/2022/day/23
"""
from itertools import chain
from datetime import datetime

def create_elf_dict(filename):
    """
    Read in the file. Create the elf position dictionary
    """
    with open(filename, encoding='UTF8') as file:
        elf_dict= {}
        elf = 1
        line_num = 0

        for line in file:
            line_num +=1
            line = line.replace('\n','')

            for pos, element in enumerate (line):
                pos+=1
                if element == '#':
                    elf_dict[elf] = ((pos,line_num))
                    elf +=1

    return elf_dict

def check_adjacency(pos,elf_dict):
    """
    Given the position, check if an elf has any adjacent elves
    """
    coord_list =[]
    for i in range(3):
        i-=1
        for j in range(3):
            j-=1
            if not(i ==0 and j==0):
                coord_list.append((pos[0]+i, pos[1]+j))

    if any(elf in elf_dict.values() for elf in coord_list):
        return True

def check_if_elf(pos, elf_dict, turn):
    """
    Give the turn determine the starting direction and
    check whether the elf can move in that direction
    """

    north_check = [(pos[0] -1,pos[1] - 1) ,(pos[0],pos[1] - 1) , (pos[0] + 1,pos[1] -1)]
    south_check = [(pos[0] -1,pos[1] + 1) ,(pos[0],pos[1] + 1) , (pos[0] + 1,pos[1] +1)]
    west_check = [(pos[0]-1,pos[1]+1) ,(pos[0]-1,pos[1]) , (pos[0]-1,pos[1]-1)]
    east_check = [(pos[0]+1,pos[1] +1)  ,(pos[0]+1,pos[1]) , (pos[0]+1,pos[1]-1)]

    order_list = [north_check,south_check,west_check,east_check]
    start_pos = turn % 4 - 1

    for idx in range(len(order_list)):
        #print  (idx, order_list[(idx + start_pos) % len(order_list)])
        coords = order_list[(idx + start_pos) % len(order_list)]
        # contains at least one of the
        if not any(elf in elf_dict.values() for elf in coords):
            return (idx + start_pos) % len(order_list)

def get_proposed_state(elf_dict, turn):
    """
    Calculate the new proposed position for each elf
    """
    elf_temp_dict = {}

    for elf, pos in elf_dict.items():
        if check_adjacency(pos,elf_dict):
            check_passed = check_if_elf(pos, elf_dict, turn)

            #North
            if check_passed == 0:
                proposed_pos = (pos[0], pos[1] - 1)
            #South
            elif check_passed == 1:
                proposed_pos = (pos[0], pos[1] + 1)
            #West
            elif check_passed == 2:
                proposed_pos = (pos[0] -1, pos[1])
            #East
            elif check_passed == 3:
                proposed_pos = (pos[0]+1, pos[1])

            if check_passed in [0,1,2,3]:
                elf_temp_dict[elf] = proposed_pos

    return elf_dict, elf_temp_dict

def move_elves(elf_dict, elf_temp_dict):
    """
    Check if the proposed position will be occupied by multiple
    elves. If so the elves remain otherwise we update their position.
    """

    rev_dict = {}
    any_move= False
    # Get all the temp positions where there are multiple elves
    for key, value in elf_temp_dict.items():
        rev_dict.setdefault(value, set()).add(key)

    multiple_pos = set(chain.from_iterable(
         values for key, values in rev_dict.items()
         if len(values) > 1))

    # update the position dictionary -
    for elf in elf_temp_dict.keys():
        # If the elf won't clash with another elf then we can move
        if elf not in multiple_pos:
            elf_dict[elf] = elf_temp_dict[elf]
            any_move = True

    return elf_dict, any_move

def count_empty_tiles(elf_dict):
    """
    This is used in part 1 to determine the mi and max
    x and y values to calculate the possible positions.
    It calculates the emoty positions by subtracting the
    number of elves
    """
    pos_list = []
    num_elves = 0
    for pos in elf_dict.values():
        pos_list.append(pos)
        num_elves+=1

    x_list, y_list = list(zip(*pos_list))
    x_len = max(x_list) - min(x_list) + 1
    y_len = max(y_list) - min(y_list) + 1
    size = x_len*y_len
    num_empty = size-num_elves

    return num_empty

def part1(elf_dict):
    """
    Run the game for 10 turns and output the number of empty tiles
    """
    for turn in range(10):
        turn+=1
        elf_dict, elf_temp_dict = get_proposed_state(elf_dict, turn)
        elf_dict = move_elves(elf_dict, elf_temp_dict)[0]
        # print(turn,any_move)
    num_empty = count_empty_tiles(elf_dict)
    print("The number of empty tiles for part 1 is ", num_empty)

def part2(elf_dict):
    """
    Run the game until no elves can move then output how many turns
    """
    any_move = True
    turn = 0

    while any_move is True:
        turn+=1
        elf_dict, elf_temp_dict = get_proposed_state(elf_dict, turn)
        elf_dict, any_move = move_elves(elf_dict, elf_temp_dict)

        if turn %50 == 0:
            print(turn,any_move, datetime.now())
    print("The number of the first round where no Elf moves is", turn)

def solve_puzzle():
    """
    Code to output part 1 and part 2
    """

    elf_dict = create_elf_dict(r'data\day23.txt')
    part1(elf_dict)
    elf_dict = create_elf_dict(r'data\day23.txt')
    part2(elf_dict)

solve_puzzle()
