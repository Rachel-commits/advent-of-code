"""
Advent of Code 2022
Day 6: Tuning Trouble
Calculate the number of characters processed
the input file
https://adventofcode.com/2022/day/6
"""

def read_file(filename):
    """
    Read in file
    """
    with open (filename, encoding = 'UTF8') as file:
        return list(file.read())

def get_start_position(input_list, num_chars):
    """
    Given an input list get the position after the first
    non duplicate number of charcters
    """
    check_list =[]
    pos = 0
    for pos, char in enumerate(input_list):
        if pos < num_chars:
            check_list.append(char)
        else:
             #  check  for dupes
            if len(set(check_list)) <  len(check_list):
                check_list.pop(0)
                check_list.append(char)
            else:
                break
    return pos

def run_puzzle():
    """
    Run part 1 - 4 distinct characters at start and
    part 2 - 14 distinct characters at stary.
    """
    input_list = read_file(r'data/day6.txt')
    pos1 = get_start_position(input_list, 4)
    pos2 = get_start_position(input_list, 14)
    print("The answer to part 1 is ", pos1)
    print("The answer to part 2 is ", pos2)
    return

run_puzzle()
