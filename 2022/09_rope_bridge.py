
"""
Advent of Code 2022
Day 9: Rope Bridge
Calculate the number od positions of the rope
https://adventofcode.com/2022/day/9
"""

from collections import defaultdict
import numpy as np

def move_rope(rope_number,head_list,tail_list, tail_visits, total_ropes):
    """
    Move each rope and update the tail visited list
    """
    relative_tail = [0,0]
    relative_tail[0] = head_list[0] - tail_list[0]
    relative_tail[1] = head_list[1] - tail_list[1]
    x_increment = np.sign(relative_tail[0])
    y_increment = np.sign(relative_tail[1])

    # move horizontal
    if abs(relative_tail[0]) >1  and abs(relative_tail[1]) == 0:
        tail_list[0] += x_increment

    #move vertical
    elif abs(relative_tail[1]) >1 and abs(relative_tail[0]) == 0:
        tail_list[1] += y_increment

        #move diagonal
    elif abs(relative_tail[0]) >1 or abs(relative_tail[1]) >1:
        tail_list[0] += x_increment
        tail_list[1] += y_increment

    if rope_number ==total_ropes -2:
        coords=(tail_list[0],tail_list[1])
        tail_visits.append(coords)
    return head_list, tail_list,tail_visits


def move_all_ropes(head_list,tail_visits,rope_dict, direction, length, num_knots):
    """
    Using the direction and length instructions iterate through all length
    uppdating the position for all the ropes
    """
    #Set positive or negative direction'
    if direction in ('R', 'U'):
        step = 1
    else:
        step=-1

    # Iterate through each step
    for i in range(length+1):
        if i>0:
            if direction in ('L','R'):
                head_list[0]+=step
            elif direction in ('U','D'):
                head_list[1]+=step

            # Iterate through each knot
            for knot in range(num_knots -1):
                if knot ==0:
                    first_list = head_list.copy()
                    follow_list = rope_dict[1][0]

                elif knot>0:
                    first_list = rope_dict[knot][0]
                    follow_list = rope_dict[knot+1][0]

                first_list,follow_list, tail_visits = move_rope(knot,
                                                                first_list,
                                                                follow_list,
                                                                tail_visits,
                                                                num_knots)
                rope_dict[knot].append(first_list)
                rope_dict[knot+1].append(follow_list)

    return head_list, tail_visits, rope_dict

def process_file(filename, num_knots):
    """
    Read in the file line by line and calculate tail visits
    """
    i=0
    hpos =[0,0]
    tpos =[0,0]
    tail_visits=[]
    coords=(tpos[0],tpos[1])
    tail_visits.append(coords)

    rope_dict = defaultdict(list)
    for i in range(10):
        rope_dict[i].append([0,0])
    with open(filename, encoding = 'UTF8') as file:
        for line in file:
            i+=1
            line = line.strip('\n')
            line = line.split(' ')
            direction = line[0]
            length = int(line[1])
            hpos, tail_visits, rope_dict = move_all_ropes(hpos,
                                                        tail_visits,
                                                        rope_dict,
                                                        direction,
                                                        length,
                                                        num_knots)

    print("The number of positions  for ", num_knots," knots is " ,len(set(tail_visits)))

# Part 1
process_file(r'data\day9.txt', 2)
# Part  2
process_file(r'data\day9.txt', 10)
