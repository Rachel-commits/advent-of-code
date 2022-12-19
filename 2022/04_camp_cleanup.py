"""
Advent of Code 2022
Day 4: Camp Cleanup
Calculating the elves with the most calories
https://adventofcode.com/2022/day/4
"""

def generate_sections(line):
    """
    From the input line generate 2 section lists
    """
    elf1, elf2 = line.strip().split(',')
    # First Elf
    start, end = elf1.split('-')
    section1 = list(range(int(start), int(end)+1))

    # Second Elf
    start, end = elf2.split('-')
    section2 = list(range(int(start), int(end)+1))

    return section1, section2

def count_overlap(filename, check_type):
    """
    Read in file and check section overlap
    Any or All depending on which part
    """
    count=0
    with open(filename, encoding = 'utf8') as file:
        for line in file:
            section1, section2 = generate_sections(line)

            if check_type == 'all':
                if all(item in section1 for item in section2) or \
                    all(item in section2 for item in section1):
                    count +=1

            elif check_type == 'any':
                if any(item in section1 for item in section2):
                    count +=1

    print("The number of sections overlapping is ", count)
    return count

count_overlap(r'data\day4.txt', 'all')
count_overlap(r'data\day4.txt', 'any')
