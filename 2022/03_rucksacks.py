"""
Advent of Code 2022
Day 3: Rucksack Reorganization
Calculating the elves with the most calories
https://adventofcode.com/2022/day/3
"""

from string import ascii_uppercase, ascii_lowercase
alphabet = {v:k+1 for k,v in enumerate(ascii_lowercase + ascii_uppercase)}

def get_priority(rucksack):
    """
    Get the items that appear in both sections and
    calculate their priority according to an alphabet
    lookup where a = 1, z = 26, A = 27 Z =52
    """
    #split compartments
    position = int(len(rucksack)/2)
    section1, section2 = rucksack[:position], rucksack[position:]

    #find common items
    shared_items = ''.join([
        item for item in section1
        if item in section2
    ])

    priority = alphabet.get(shared_items[0])
    return priority

def get_badge_priority(bag1, bag2, bag3):
    """
    Get the items that appear in both sections and
    calculate their priority according to an alphabet
    lookup where a = 1, z = 26, A = 27 Z =52
    """

    shared_items1 = ''.join([
        item for item in bag1
        if item in bag2
    ])

    shared_items2 = ''.join([
        item for item in shared_items1
        if item in bag3
    ])

    priority = alphabet.get(shared_items2[0])
    return priority

def process_bags(filename, part):
    """
    Read in the bags and get the priority.
    For part we also need to get the badge
    """

    line_num = 1
    priority = 0
    with open(filename, encoding = 'utf8') as file:
        for rucksack in file:
            rucksack = rucksack.rstrip('\n')

            if part == 'part1':
                priority += get_priority(rucksack)
            elif part == 'part2':
                if line_num %3 ==1:
                    rucksack1= rucksack
                elif line_num %3 ==2:
                    rucksack2= rucksack
                elif line_num %3 ==0:
                    rucksack3= rucksack
                    priority +=get_badge_priority(rucksack1, rucksack2, rucksack3)
                line_num += 1

    print("The ", part, " priority score is: ", priority)

process_bags(r'data\day3.txt','part1')
process_bags(r'data\day3.txt','part2')
