"""
Advent of Code 2024
Day 1: Historian Hysteria
What is the sum of all of the calibration values?
https://adventofcode.com/2024/day/1
"""
from collections import Counter

def import_file(filename: str):
    list1 = []
    list2 = []

    with open(filename, 'r') as file:
        for line in file:
            list1.append(int(line.split()[0]))
            list2.append(int(line.split()[1]))
    
    return list1, list2

def solve_part1(list1,list2): 

    difference=0
    list1.sort()
    list2.sort()
    for idx, element  in enumerate(list1):
        difference+= abs(list1[idx] -list2[idx])
    
    print("The answer to part 1 is: ", difference)

def solve_part2(list1,list2):
    
    similarity_score=0
    score_dict = Counter(list2)

    for element  in list1:
        if score_dict.get(element) is not None:
            similarity_score+=element*score_dict.get(element)
    print("The answer to part 2 is: ", similarity_score)


def main():
    list1, list2 = import_file('2024/data/day1.txt')
    solve_part1(list1, list2)
    solve_part2(list1, list2)
    

# Entry point for running the puzzle solving process
if __name__ == '__main__':
    main()
